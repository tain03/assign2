from .models import Cart

class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            cart = None
            if request.session.get('cart_id'):
                try:
                    cart = Cart.objects.get(id=request.session['cart_id'])
                except Cart.DoesNotExist:
                    pass
            if not cart:
                cart = Cart.objects.create(session_key=request.session.session_key)
                request.session['cart_id'] = cart.id

        request.cart = cart
        response = self.get_response(request)
        return response 