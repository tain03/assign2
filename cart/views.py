from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from products.models import Product
from .models import Cart, CartItem

def cart_detail(request):
    cart = request.cart
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.cart
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity <= 0:
        messages.error(request, 'Invalid quantity.')
        return redirect('cart:cart_detail')
    
    if quantity > product.stock_quantity:
        messages.error(request, 'Not enough stock available.')
        return redirect('cart:cart_detail')
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    if not created:
        cart_item.quantity += quantity
        if cart_item.quantity > product.stock_quantity:
            messages.error(request, 'Not enough stock available.')
            return redirect('cart:cart_detail')
        cart_item.save()
    
    messages.success(request, f'{product.name} added to cart.')
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = request.cart
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    messages.success(request, f'{product.name} removed from cart.')
    return redirect('cart:cart_detail')

def cart_update(request, product_id):
    if request.method == 'POST':
        cart = request.cart
        product = get_object_or_404(Product, id=product_id)
        cart_item = get_object_or_404(CartItem, cart=cart, product=product)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity <= 0:
            cart_item.delete()
            return JsonResponse({'status': 'success', 'message': 'Item removed from cart.'})
        
        if quantity > product.stock_quantity:
            return JsonResponse({
                'status': 'error',
                'message': 'Not enough stock available.'
            })
        
        cart_item.quantity = quantity
        cart_item.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Cart updated successfully.',
            'total_price': cart_item.total_price,
            'cart_total': cart.total_price
        })
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}) 