from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Custom form for Product model with improved widgets."""
    
    class Meta:
        model = Product
        fields = [
            'name', 
            'description', 
            'category',
            'image',
            'price', 
            'original_price',
            'rating', 
            'pros', 
            'cons',
            'affiliate_url',
            'is_featured'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product Name',
                'maxlength': '255'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Product description'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'original_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00 (optional)',
                'step': '0.01'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0-5',
                'step': '0.1',
                'min': '0',
                'max': '5'
            }),
            'pros': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Comma-separated pros (e.g., Fast, Affordable, Reliable)'
            }),
            'cons': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Comma-separated cons (e.g., Limited warranty, Slow shipping)'
            }),
            'affiliate_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com/product',
                'maxlength': '500'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
    
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        original_price = cleaned_data.get('original_price')
        
        if price and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        
        if original_price and original_price < 0:
            raise forms.ValidationError("Original price cannot be negative.")
        
        if price and original_price and price > original_price:
            raise forms.ValidationError("Price must be less than or equal to original price.")
        
        return cleaned_data


class CategoryForm(forms.ModelForm):
    """Custom form for Category model."""
    
    class Meta:
        model = Category
        fields = ['name', 'description', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category Name',
                'maxlength': '200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Category description'
            }),
            'icon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Font Awesome icon class (e.g., fa-laptop)'
            })
        }
