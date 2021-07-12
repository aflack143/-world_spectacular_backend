from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Country, Country_Picture, User, User_Visit
import json
import http.client
# from restcountries import RestCountryApiV2 as rapi

def landing_page(request):
    print('Testing')
    return HttpResponse()

def get_countries(request):
    all_countries = Country.objects.all()
    parsed_all_countries = serialize('json', all_countries)
    return HttpResponse(parsed_all_countries, content_type='application/json')

def get_all_countries_photos(request):
    all_countries_photos = Country_Picture.objects.all()
    parsed_all_countries_photos = serialize('json', all_countries_photos)
    return HttpResponse(parsed_all_countries_photos, content_type='application/json')