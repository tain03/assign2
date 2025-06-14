from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Order, OrderItem
from cart.models import Cart, CartItem

@login_required
def checkout(request):
    cart = request.cart
    
    if not cart.items.exists():
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:cart_detail')
    
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Create order
                order = Order.objects.create(
                    user=request.user,
                    email=request.POST.get('email'),
                    phone=request.POST.get('phone'),
                    shipping_address=request.POST.get('shipping_address'),
                    billing_address=request.POST.get('billing_address'),
                    total_amount=cart.total_price
                )
                
                # Create order items
                for cart_item in cart.items.all():
                    if cart_item.quantity > cart_item.product.stock_quantity:
                        raise ValueError(f'Not enough stock for {cart_item.product.name}')
                    
                    OrderItem.objects.create(
                        order=order,
                        product=cart_item.product,
                        quantity=cart_item.quantity,
                        price_at_time=cart_item.product.price
                    )
                    
                    # Update stock
                    cart_item.product.stock_quantity -= cart_item.quantity
                    cart_item.product.save()
                
                # Clear cart
                cart.items.all().delete()
                
                messages.success(request, 'Order placed successfully!')
                return redirect('orders:order_detail', order_id=order.id)
                
        except ValueError as e:
            messages.error(request, str(e))
            return redirect('cart:cart_detail')
        except Exception as e:
            messages.error(request, 'An error occurred while processing your order.')
            return redirect('cart:cart_detail')
    
    return render(request, 'orders/checkout.html', {'cart': cart})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders}) 