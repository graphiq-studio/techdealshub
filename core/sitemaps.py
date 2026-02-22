from django.contrib.sitemaps import Sitemap
from products.models import Product, Category
from blog.models import BlogPost


class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Product.objects.all()

    def lastmod(self, item):
        return item.updated_at


class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Category.objects.all()


class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return BlogPost.objects.filter(is_published=True)

    def lastmod(self, item):
        return item.updated_at


sitemaps = {
    'products': ProductSitemap,
    'categories': CategorySitemap,
    'blogs': BlogSitemap,
}
