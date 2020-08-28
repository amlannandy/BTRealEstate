from django.urls import path

from . import views

# /listings
# listings/:id
urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
