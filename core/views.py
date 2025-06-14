from django.shortcuts import render
from products.models import Product, Category

def home(request):
    featured_products = Product.objects.filter(is_active=True)[:8]
    categories = Category.objects.filter(is_active=True, parent_category=None)
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html') 