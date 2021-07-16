from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('world/', views.get_world, name='get_world'),
    path('world/photos/', views.get_world_photos, name='get_world_photos'),
    path('country/<int:cpk>/', views.get_country, name='get_country'),
    path('country/<int:cpk>/photos/', views.get_country_photos, name='get_country_photos'),
    path('profiles/', views.get_users, name='get_users'),
    path('profiles/<str:token>/', views.get_user, name='get_user'),
    path('profiles/create/', views.create_user_profile, name='create_user_profile'),
    path('profiles/<str:token>/delete/', views.delete_user_profile, name='delete_user_profile'),

    path('profiles/<str:token>/visited/', views.get_user_visited, name='get_user_visit'),
    path('profiles/<str:token>/dream_visit/', views.get_user_dream_visit, name='get_user_visit'),
    path('profiles/<str:token>/<int:cpk>/', views.user_visited, name='user_visited'),
    path('profiles/<str:token>/<int:cpk>/', views.user_dream_visit, name='user_dream_visit'),
]