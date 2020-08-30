from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    my_listings = Listing.objects.order_by(
        '-list_date').filter(isPublished=True)
    if len(my_listings) >= 3:
        my_listings = my_listings[:3]
    context = {
        'listings': my_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('name')
    realtor = realtors.filter(is_mvp=True)[0]
    context = {
        'realtors': realtors,
        'realtor': realtor,
    }
    return render(request, 'pages/about.html', context)
