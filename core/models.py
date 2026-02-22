from django.db import models


class SiteConfig(models.Model):
    """Global site configuration."""
    site_name = models.CharField(max_length=255, default="TechDealsHub")
    site_description = models.TextField(default="Find the best tech products and affiliate deals")
    logo = models.ImageField(upload_to='site/', null=True, blank=True)
    favicon = models.ImageField(upload_to='site/', null=True, blank=True)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    # Social
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    
    # SEO
    og_image = models.ImageField(upload_to='site/', null=True, blank=True)
    google_analytics_id = models.CharField(max_length=50, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return self.site_name

    @classmethod
    def get_config(cls):
        """Get or create site config."""
        config, _ = cls.objects.get_or_create(pk=1)
        return config
