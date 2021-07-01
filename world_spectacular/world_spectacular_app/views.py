from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
import json
# from restcountries import RestCountryApiV2 as rapi


def landing_page(request):
    print('Testing')
    return HttpResponse()

# def get_countries(request):
#     # countries_all = rapi.get_all()
#     # parsed_countries_all = serialize('json', countries_all)
#     # print(parsed_countries_all)
#     return HttpResponse(countries_all, content_type='application/json')