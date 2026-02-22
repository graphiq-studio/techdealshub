from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Click
from .forms import ProductForm, CategoryForm
from .csv_export import clicks_export_csv, products_export_csv


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ['name', 'product_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Products Count'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = [
        'name', 
        'category', 
        'price', 
        'rating', 
        'click_count', 
        'views_count',
        'is_featured',
        'product_image',
        'created_at'
    ]
    list_filter = [
        'category', 
        'is_featured', 
        'rating',
        'created_at',
        'updated_at'
    ]
    search_fields = ['name', 'description', 'slug']
    readonly_fields = [
        'slug',
        'click_count', 
        'views_count',
        'created_at', 
        'updated_at',
        'product_image'
    ]
    
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'category', 'description', 'image', 'product_image')
        }),
        ('Pricing', {
            'fields': ('price', 'original_price')
        }),
        ('Rating & Content', {
            'fields': ('rating', 'pros', 'cons')
        }),
        ('Affiliate & Analytics', {
            'fields': ('affiliate_url', 'click_count', 'views_count', 'is_featured')
        }),
        ('Metadata', {
            'fields': ('slug', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def product_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="border-radius: 5px;" />',
                obj.image.url
            )
        return 'No Image'
    product_image.short_description = 'Product Image'

    actions = ['mark_as_featured', 'remove_from_featured', products_export_csv]

    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} products marked as featured.')
    mark_as_featured.short_description = "Mark selected as featured"

    def remove_from_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} products removed from featured.')
    remove_from_featured.short_description = "Remove from featured"


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ['product', 'ip_address', 'created_at']
    list_filter = ['product', 'created_at']
    search_fields = ['product__name', 'ip_address']
    readonly_fields = [
        'product', 
        'ip_address', 
        'user_agent', 
        'referrer', 
        'created_at'
    ]
    date_hierarchy = 'created_at'
    actions = [clicks_export_csv]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
