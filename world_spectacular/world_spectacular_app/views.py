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

def get_country(request, cpk):
    country = Country.objects.filter(id=cpk)
    print(country)
    parsed_each_country = serialize('json', country)
    return HttpResponse(parsed_each_country, content_type='application/json')

def get_country_photos(request, cpk):
    found_country_photo = Country_Picture.objects.filter(country=cpk)
    print(found_country_photo)
    parsed_each_country_photos = serialize('json', found_country_photo)
    return HttpResponse(parsed_each_country_photos, content_type='application/json')

def get_users(request):
    users = User.objects.all()
    parsed_users = serialize('json', users)
    return HttpResponse(parsed_users, content_type='application/json')

def get_user(request, upk):
    user = User.objects.get(id=upk)
    print(user)
    parsed_user = serialize('json', [user])
    # return HttpResponse()
    return HttpResponse(parsed_user, content_type='application/json')

def create_user(request):
    print(request.body)
    parsed_body = request.body.decode('utf-8')
    print(parsed_body)
    # parsed_body = json.loads(parsed_body)
    parsed_body = parsed_body['data']
    user = User(token=parsed_body["token"], username=parsed_body["username"], photo_url=parsed_body["photo_url"], about_me=parsed_body["about_me"], country=parsed_body["country"])
    user.save()
    parsed_user = serialize('json', [user])
    return HttpResponse(parsed_user, content_type='application/json')
    # return HttpResponse()




# user = User(token=parsed_body['token'], username=parsed_body['username'], photo_url=parsed_body['photo_url'], about_me=parsed_body['about_me'], country=parsed_body['country'])
    # user.save()
    # parsed_user = serialize('json', [user])
    # return HttpResponse(parsed_user, content_type='application/json')