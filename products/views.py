from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from .models import Product, Category, Click
from blog.models import BlogPost
from core.utilities import get_client_ip, get_user_agent, get_referrer


def home(request):
    """Homepage view."""
    featured_products = Product.objects.filter(is_featured=True).select_related('category')[:6]
    top_rated_products = Product.objects.all().order_by('-rating')[:6]
    latest_blogs = BlogPost.objects.filter(is_published=True).order_by('-published_at')[:3]
    categories = Category.objects.all()

    context = {
        'featured_products': featured_products,
        'top_rated_products': top_rated_products,
        'latest_blogs': latest_blogs,
        'categories': categories,
    }
    return render(request, 'products/home.html', context)


def category_list(request):
    """List all categories."""
    categories = Category.objects.annotate(product_count=Count('products'))
    context = {'categories': categories}
    return render(request, 'products/category_list.html', context)


def category_detail(request, slug):
    """Category detail page with products."""
    category = get_object_or_404(Category, slug=slug)
    
    products = Product.objects.filter(category=category).select_related('category')
    
    # Filter by rating if specified
    min_rating = request.GET.get('min_rating')
    if min_rating:
        products = products.filter(rating__gte=float(min_rating))
    
    # Sort options
    sort = request.GET.get('sort', '-created_at')
    if sort in ['price', '-price', 'rating', '-rating', '-created_at']:
        products = products.order_by(sort)
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'category': category,
        'products': products,
        'sort': sort,
    }
    return render(request, 'products/category_detail.html', context)


def product_detail(request, slug):
    """Product detail page."""
    product = get_object_or_404(Product, slug=slug)
    
    # Increment view count
    product.views_count += 1
    product.save(update_fields=['views_count'])
    
    # Get related products
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)


def product_search(request):
    """Search products."""
    query = request.GET.get('q', '').strip()
    products = Product.objects.select_related('category')
    
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(pro__icontains=query)
        ).distinct()
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'products/search_results.html', context)


@require_http_methods(["GET"])
def affiliate_redirect(request, product_id):
    """Redirect to affiliate URL and log the click."""
    product = get_object_or_404(Product, id=product_id)
    
    # Log the click
    Click.objects.create(
        product=product,
        ip_address=get_client_ip(request),
        user_agent=get_user_agent(request),
        referrer=get_referrer(request),
    )
    
    # Increment click count
    product.click_count += 1
    product.save(update_fields=['click_count'])
    
    # Redirect to affiliate URL
    return redirect(product.affiliate_url)


def page_not_found(request, exception=None):
    """404 error handler."""
    return render(request, 'errors/404.html', status=404)


def page_error(request, exception=None):
    """500 error handler."""
    return render(request, 'errors/500.html', status=500)
