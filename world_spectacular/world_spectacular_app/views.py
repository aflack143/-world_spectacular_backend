from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Country, Country_Picture, User, User_Visit
from django.shortcuts import get_object_or_404
import json
import http.client
# from restcountries import RestCountryApiV2 as rapi

def landing_page(request):
    print('Testing')
    return HttpResponse()

def get_world(request):
    world = Country.objects.all()
    parsed_world = serialize('json', world)
    return HttpResponse(parsed_world, content_type='application/json')

def get_world_photos(request):
    world_photos = Country_Picture.objects.all()
    parsed_world_photos = serialize('json', world_photos)
    return HttpResponse(parsed_world_photos, content_type='application/json')

def get_country(request, pk):
    country = Country.objects.filter(id=pk)
    print(country)
    parsed_each_country = serialize('json', country)
    return HttpResponse(parsed_each_country, content_type='application/json')

def get_country_photos(request, pk):
    found_country_photo = Country_Picture.objects.filter(country=pk)
    print(found_country_photo)
    parsed_each_country_photos = serialize('json', found_country_photo)
    return HttpResponse(parsed_each_country_photos, content_type='application/json')