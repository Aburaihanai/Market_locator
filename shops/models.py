from django.db import models

CATEGORY_CHOICES = [
    ('clothing', 'Clothing & Fashion'),
    ('foodstuff', 'Foodstuff'),
    ('electronics', 'Electronics'),
    ('building', 'Building Materials'),
    ('tools', 'Tools & Spare Parts'),
    ('cosmetics', 'Cosmetics & Beauty'),
    ('phones', 'Phones & Accessories'),
    ('others', 'Others'),
]

class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_number = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    section = models.CharField(max_length=100, help_text="E.g., Block A, Row 2, Opp. Gate")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    products = models.TextField(help_text="List of products or services sold")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='shop_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid_ad = models.BooleanField(default=False)
    ad_banner = models.ImageField(upload_to='ads/', blank=True, null=True)
    paid_till = models.DateField(null=True, blank=True)
    payment_verified = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.shop_name} ({self.shop_number})"
