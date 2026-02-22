from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost
from products.csv_export import blog_export_csv


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status_badge',
        'author',
        'views_count',
        'featured_image_preview',
        'published_at'
    ]
    list_filter = [
        'is_published',
        'created_at',
        'published_at',
        'author'
    ]
    search_fields = ['title', 'content', 'slug']
    readonly_fields = [
        'slug',
        'views_count',
        'created_at',
        'updated_at',
        'featured_image_preview'
    ]

    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'author', 'content')
        }),
        ('Media', {
            'fields': ('featured_image', 'featured_image_preview')
        }),
        ('SEO & Excerpt', {
            'fields': ('excerpt', 'meta_description')
        }),
        ('Publishing', {
            'fields': ('is_published', 'published_at')
        }),
        ('Analytics', {
            'fields': ('views_count',)
        }),
        ('Metadata', {
            'fields': ('slug', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def featured_image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" width="200" height="150" style="border-radius: 5px;" />',
                obj.featured_image.url
            )
        return 'No Image'
    featured_image_preview.short_description = 'Featured Image Preview'

    def status_badge(self, obj):
        if obj.is_published:
            return format_html(
                '<span style="color: white; background-color: green; padding: 3px 10px; border-radius: 3px;">Published</span>'
            )
        return format_html(
            '<span style="color: white; background-color: orange; padding: 3px 10px; border-radius: 3px;">Draft</span>'
        )
    status_badge.short_description = 'Status'

    actions = ['publish_posts', 'unpublish_posts', blog_export_csv]

    def publish_posts(self, request, queryset):
        from django.utils import timezone
        updated = queryset.update(is_published=True, published_at=timezone.now())
        self.message_user(request, f'{updated} posts published.')
    publish_posts.short_description = "Publish selected posts"

    def unpublish_posts(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f'{updated} posts unpublished.')
    unpublish_posts.short_description = "Unpublish selected posts"
