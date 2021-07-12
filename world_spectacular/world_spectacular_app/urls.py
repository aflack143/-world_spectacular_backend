from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('world/', views.get_countries, name='get_countries'),
    path('world/photos', views.get_all_countries_photos, name='get_all_countries_photos'),
    # path('country/:abbr/', views.get_country, name='get_user'),
    # path('profiles/', views.get_users, name='get_users'),
    # path('profiles/:pk/', views.get_user, name='get_user'),
]