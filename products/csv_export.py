import csv
from datetime import datetime
from django.http import HttpResponse


def export_to_csv(model_name, queryset, fields):
    """
    Generic function to export queryset to CSV file.
    
    Args:
        model_name: Name of the model for filename
        queryset: QuerySet to export
        fields: List of field names to include
    
    Returns:
        HttpResponse with CSV file
    """
    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'{model_name}_{timestamp}.csv'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    # Create CSV writer
    writer = csv.writer(response)
    
    # Write header
    writer.writerow(fields)
    
    # Write data rows
    for obj in queryset:
        row = []
        for field in fields:
            # Handle related fields using __ notation
            if '__' in field:
                parts = field.split('__')
                value = obj
                for part in parts:
                    value = getattr(value, part, '')
                row.append(value)
            else:
                row.append(getattr(obj, field, ''))
        writer.writerow(row)
    
    return response


def clicks_export_csv(modeladmin, request, queryset):
    """Export clicks to CSV."""
    fields = [
        'product__name',
        'ip_address',
        'user_agent',
        'referrer',
        'created_at'
    ]
    return export_to_csv('affiliate_clicks', queryset, fields)

clicks_export_csv.short_description = "Download selected clicks as CSV"


def products_export_csv(modeladmin, request, queryset):
    """Export products to CSV."""
    fields = [
        'name',
        'category__name',
        'price',
        'original_price',
        'rating',
        'click_count',
        'views_count',
        'is_featured',
        'created_at'
    ]
    return export_to_csv('products', queryset, fields)

products_export_csv.short_description = "Download selected products as CSV"


def blog_export_csv(modeladmin, request, queryset):
    """Export blog posts to CSV."""
    fields = [
        'title',
        'slug',
        'is_published',
        'published_at',
        'created_at'
    ]
    return export_to_csv('blog_posts', queryset, fields)

blog_export_csv.short_description = "Download selected blog posts as CSV"
