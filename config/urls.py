"""
URL configuration for techdealshub project.
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.sitemaps import sitemaps
from core.views import RobotsView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Apps
    path('', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('', include('core.urls')),

    # SEO
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', RobotsView.as_view(), name='robots'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Error handlers
handler404 = 'products.views.page_not_found'
handler500 = 'products.views.page_error'
