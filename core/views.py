from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from products.models import Category


class RobotsView(TemplateView):
    """Robots.txt view."""
    template_name = 'robots.txt'
    content_type = 'text/plain'


def sitemap_index(request):
    """Sitemap index view."""
    return render(request, 'sitemap_index.xml', content_type='application/xml')


@require_http_methods(["GET"])
def about(request):
    """About page."""
    categories = Category.objects.all()
    context = {'categories': categories}
    from django.shortcuts import render
    return render(request, 'core/about.html', context)


@require_http_methods(["GET"])
def privacy(request):
    """Privacy policy page."""
    from django.shortcuts import render
    return render(request, 'core/privacy.html')


@require_http_methods(["GET"])
def terms(request):
    """Terms and conditions page."""
    from django.shortcuts import render
    return render(request, 'core/terms.html')


@require_http_methods(["GET"])
def contact(request):
    """Contact page."""
    from django.shortcuts import render
    return render(request, 'core/contact.html')
