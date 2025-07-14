from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'shop_name', 'shop_number', 'owner_name', 'section',
            'category', 'products', 'phone_number', 'image',
            'is_paid_ad', 'ad_banner', 'paid_till', 'payment_verified'
        ]
        widgets = {
            'products': forms.Textarea(attrs={'rows': 3}),
        }
