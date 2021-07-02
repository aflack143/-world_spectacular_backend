from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    # path('profiles/', views.get_users, name='get_users'),
    # path('profiles/:pk/', views.get_user, name='get_user'),
    # path('country/:abbr/', views.get_user, name='get_user'),
    # path('world/', views.get_countries, name='get_countries'),
]