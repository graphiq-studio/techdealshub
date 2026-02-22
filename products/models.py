from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    """Category model for organizing products."""
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="Font awesome icon class")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """Product model for affiliate marketing."""
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True, 
        help_text="Original price before discount"
    )
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        default=4.5,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    image = models.ImageField(upload_to='products/%Y/%m/')
    affiliate_url = models.URLField(max_length=500)
    pros = models.TextField(blank=True, null=True, help_text="Comma separated pros")
    cons = models.TextField(blank=True, null=True, help_text="Comma separated cons")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    is_featured = models.BooleanField(default=False, db_index=True)
    click_count = models.PositiveIntegerField(default=0, db_index=True)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_featured', '-created_at']),
            models.Index(fields=['category', '-created_at']),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def discount_percentage(self):
        """Calculate discount percentage if original price is set."""
        if self.original_price and self.price < self.original_price:
            discount = ((self.original_price - self.price) / self.original_price) * 100
            return round(discount, 0)
        return 0

    @property
    def pros_list(self):
        """Return pros as a list."""
        return [pro.strip() for pro in self.pros.split(',') if pro.strip()] if self.pros else []

    @property
    def cons_list(self):
        """Return cons as a list."""
        return [con.strip() for con in self.cons.split(',') if con.strip()] if self.cons else []


class Click(models.Model):
    """Model to track affiliate link clicks."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='clicks')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, null=True)
    referrer = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Click"
        verbose_name_plural = "Clicks"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['product', '-created_at']),
        ]

    def __str__(self):
        return f"{self.product.name} - {self.created_at}"
