from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from products.models import Category, Product
from blog.models import BlogPost
from core.models import SiteConfig
from django.utils import timezone
from decimal import Decimal
import os


class Command(BaseCommand):
    help = 'Seed database with initial data for development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))

        # Create superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('✓ Admin user created'))

        # Create site config
        if not SiteConfig.objects.exists():
            SiteConfig.objects.create(
                site_name='TechDealsHub',
                site_description='Find the best tech products and affiliate deals',
                contact_email='contact@techdealshub.com',
                keywords='tech, gadgets, affiliate, deals, AliExpress'
            )
            self.stdout.write(self.style.SUCCESS('✓ Site configuration created'))

        # Create categories
        categories_data = [
            {
                'name': 'Smartphones & Accessories',
                'icon': 'fa-mobile-alt',
                'description': 'Latest smartphones, phone cases, and mobile accessories'
            },
            {
                'name': 'Laptops & Computers',
                'icon': 'fa-laptop',
                'description': 'Laptops, tablets, and computer accessories'
            },
            {
                'name': 'Audio & Speakers',
                'icon': 'fa-headphones',
                'description': 'Headphones, speakers, and audio equipment'
            },
            {
                'name': 'Wearables',
                'icon': 'fa-watch',
                'description': 'Smartwatches, fitness trackers, and health devices'
            },
            {
                'name': 'Gaming',
                'icon': 'fa-gamepad',
                'description': 'Gaming peripherals, consoles, and accessories'
            },
            {
                'name': 'Home & Smart Devices',
                'icon': 'fa-home',
                'description': 'Smart home devices, IoT gadgets, and home automation'
            },
        ]

        categories = {}
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'icon': cat_data['icon'],
                }
            )
            categories[cat_data['name']] = cat
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Category created: {cat.name}'))

        # Create sample products
        products_data = [
            {
                'name': 'Premium Wireless Earbuds Pro',
                'price': Decimal('45.99'),
                'original_price': Decimal('89.99'),
                'rating': Decimal('4.8'),
                'description': 'High-quality wireless earbuds with active noise cancellation, 30-hour battery life, and premium sound quality.',
                'pros': 'Great sound quality, Long battery life, Comfortable fit, Affordable',
                'cons': 'Plastic build, Limited color options',
                'category': categories.get('Audio & Speakers'),
                'is_featured': True,
            },
            {
                'name': 'Ultra-Fast USB 3.0 Flash Drive 256GB',
                'price': Decimal('28.50'),
                'original_price': Decimal('49.99'),
                'rating': Decimal('4.6'),
                'description': 'Lightning-fast data transfer speeds up to 120MB/s. Perfect for backing up files, transferring documents, or storing media.',
                'pros': 'Fast transfer speeds, Large capacity, Durable, Compact',
                'cons': 'May overheat during extended use, Some compatibility issues on older systems',
                'category': categories.get('Laptops & Computers'),
                'is_featured': True,
            },
            {
                'name': 'Smartwatch Fitness Tracker',
                'price': Decimal('79.99'),
                'original_price': Decimal('149.99'),
                'rating': Decimal('4.5'),
                'description': 'Full-featured smartwatch with heart rate monitoring, sleep tracking, and fitness modes for all activities.',
                'pros': 'Accurate tracking, Long battery, Beautiful display, Water resistant',
                'cons': 'Limited app ecosystem, Occasional syncing issues',
                'category': categories.get('Wearables'),
                'is_featured': True,
            },
            {
                'name': 'Portable Phone Stand',
                'price': Decimal('12.99'),
                'original_price': Decimal('24.99'),
                'rating': Decimal('4.3'),
                'description': 'Universal portable phone stand for all smartphones. Adjustable angles, stable grip, perfect for streaming and video calls.',
                'pros': 'Universal compatibility, Lightweight, Affordable, Adjustable',
                'cons': 'Plastic material, Small base',
                'category': categories.get('Smartphones & Accessories'),
            },
            {
                'name': 'Mechanical Gaming Keyboard RGB',
                'price': Decimal('69.99'),
                'original_price': Decimal('129.99'),
                'rating': Decimal('4.7'),
                'description': 'Professional mechanical gaming keyboard with customizable RGB lighting, programmable keys, and high-speed switches.',
                'pros': 'Excellent build quality, Responsive switches, Great for gaming, Customizable',
                'cons': 'Loud clicks, Bulky, Expensive',
                'category': categories.get('Gaming'),
                'is_featured': True,
            },
        ]

        for prod_data in products_data:
            prod, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    **prod_data,
                    'affiliate_url': 'https://www.awin1.com/cclick.php?p=example',
                    'click_count': 0,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Product created: {prod.name}'))

        # Create sample blog posts
        blog_data = [
            {
                'title': '10 Best Budget Tech Gadgets in 2024',
                'content': '<p>Looking for affordable tech gadgets that don\'t compromise on quality? Here are our top 10 picks for 2024 that offer great value for money.</p><p>From wireless earbuds to USB drives, these products deliver impressive performance at budget-friendly prices.</p>',
                'excerpt': 'Discover the best affordable tech gadgets that won\'t break your budget in 2024.',
                'meta_description': 'Top 10 budget-friendly tech gadgets of 2024 with great features and affordability.',
            },
            {
                'title': 'Complete Guide to Wireless Earbuds',
                'content': '<p>Wireless earbuds have become an essential tech accessory. This comprehensive guide covers everything you need to know before making your purchase.</p><p>We\'ll discuss battery life, sound quality, noise cancellation, and comfort factors.</p>',
                'excerpt': 'Everything you need to know about choosing the perfect wireless earbuds for your needs.',
                'meta_description': 'Complete guide to wireless earbuds - features, quality, and buying tips.',
            },
            {
                'title': 'Smartwatch Buying Guide: What to Look For',
                'content': '<p>Smartwatches offer incredible functionality beyond telling time. Learn what features matter most for your lifestyle.</p><p>From fitness tracking to notification management, find the perfect smartwatch for you.</p>',
                'excerpt': 'A comprehensive guide to choosing the right smartwatch based on your lifestyle and needs.',
                'meta_description': 'Smartwatch buying guide - features, brands, and recommendations for every budget.',
            },
        ]

        admin_user = User.objects.get(username='admin')
        for blog in blog_data:
            post, created = BlogPost.objects.get_or_create(
                title=blog['title'],
                defaults={
                    **blog,
                    'author': admin_user,
                    'is_published': True,
                    'published_at': timezone.now(),
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Blog post created: {post.title}'))

        self.stdout.write(self.style.SUCCESS('\n✓ Database seeding completed successfully!'))
        self.stdout.write(self.style.WARNING('\nLogin credentials:'))
        self.stdout.write(self.style.WARNING('  Username: admin'))
        self.stdout.write(self.style.WARNING('  Password: admin123'))
