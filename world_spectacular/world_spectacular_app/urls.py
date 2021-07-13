from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('world/', views.get_world, name='get_world'),
    path('world/photos', views.get_world_photos, name='get_world_photos'),
    path('country/<int:pk>/', views.get_country, name='get_country'),
    path('country/<int:pk>/photos/', views.get_country_photos, name='get_country_photos'),
    # path('profiles/', views.get_users, name='get_users'),
    # path('profiles/:pk/', views.get_user, name='get_user'),
]