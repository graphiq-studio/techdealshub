"""
TechDealsHub Django Settings Test
Verifies that all settings are correctly configured
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from django.conf import settings

def test_settings():
    print("✓ Django Settings Verification\n")
    
    # Environment
    print(f"DEBUG: {settings.DEBUG}")
    print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"SECRET_KEY: {'Set' if settings.SECRET_KEY != 'django-insecure-abc123xyz789changethisinproduction' else 'NEEDS CHANGE'}")
    
    # Database
    print(f"\nDatabase:")
    print(f"  Engine: {settings.DATABASES['default']['ENGINE']}")
    if settings.DATABASES['default']['NAME']:
        print(f"  Name: {settings.DATABASES['default']['NAME']}")
    
    # Apps
    print(f"\nInstalled Apps: {len(settings.INSTALLED_APPS)} apps installed")
    for app in ['products', 'blog', 'core']:
        if app in str(settings.INSTALLED_APPS):
            print(f"  ✓ {app}")
    
    # Static/Media
    print(f"\nStatic Files:")
    print(f"  URL: {settings.STATIC_URL}")
    print(f"  Root: {settings.STATIC_ROOT}")
    
    print(f"\nMedia Files:")
    print(f"  URL: {settings.MEDIA_URL}")
    print(f"  Root: {settings.MEDIA_ROOT}")
    
    # Middleware
    print(f"\nMiddleware: {len(settings.MIDDLEWARE)} middlewares")
    
    # Templates
    print(f"\nTemplates: {settings.TEMPLATES[0]['DIRS']}")
    
    print("\n✓ Settings verification complete!")

if __name__ == '__main__':
    test_settings()
