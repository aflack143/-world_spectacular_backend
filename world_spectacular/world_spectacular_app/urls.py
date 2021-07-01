from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    # path('world/', views.get_countries, name='get_countries'),
]