from django.shortcuts import render, get_object_or_404
from .models import Shop
from django.db.models import Q
from .forms import ShopForm
from django.contrib import messages
from django.shortcuts import redirect
from datetime import date
import random
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render
from .models import Shop
from datetime import date
import random

def home(request):
    today = date.today()

    # ✅ Filter only active, paid, verified ads
    featured_ads = list(Shop.objects.filter(
        is_paid_ad=True,
        payment_verified=True,
        paid_till__gte=today  # Not expired
    ).exclude(ad_banner=''))

    # ✅ Shuffle the ads to rotate randomly
    random.shuffle(featured_ads)
    featured_ads = featured_ads[:5]

    # ✅ Get all shops to display below the ads
    all_shops = Shop.objects.all().order_by('shop_name')

    return render(request, 'shops/index.html', {
        'shops': all_shops,
        'featured_ads': featured_ads
    })


def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    return render(request, 'shops/detail.html', {'shop': shop})

def search_shops(request):
    query = request.GET.get('q')
    shops = Shop.objects.filter(
        Q(shop_name__icontains=query) |
        Q(shop_number__icontains=query) |
        Q(products__icontains=query)
    ) if query else []
    return render(request, 'shops/search.html', {'shops': shops, 'query': query})

def add_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save()
            messages.success(request, 'Shop added successfully!')
            return redirect('shop_detail', shop_id=shop.id)
    else:
        form = ShopForm()
    return render(request, 'shops/add_shop.html', {'form': form})

def make_payment(request, shop_id):
    shop = Shop.objects.get(id=shop_id)

    # ✅ Simulate payment success
    shop.payment_verified = True
    shop.paid_till = timezone.now().date().replace(year=timezone.now().year + 1)  # expires in 1 year
    shop.save()

    return render(request, 'shops/payment_success.html', {'shop': shop})

