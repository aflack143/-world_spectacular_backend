from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Country, Country_Picture, User, User_Visit
from django.shortcuts import get_object_or_404
import json

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
    parsed_each_country = serialize('json', country)
    return HttpResponse(parsed_each_country, content_type='application/json')

def get_country_photos(request, cpk):
    found_country_photo = Country_Picture.objects.filter(country=cpk)
    parsed_each_country_photos = serialize('json', found_country_photo)
    return HttpResponse(parsed_each_country_photos, content_type='application/json')

def get_users(request):
    users = User.objects.all()
    parsed_users = serialize('json', users)
    return HttpResponse(parsed_users, content_type='application/json')

def get_user(request, token):
    user = User.objects.get(token=token)
    parsed_user = serialize('json', [user])
    return HttpResponse(parsed_user, content_type='application/json')

def create_user_profile(request):
    parsed_body = request.body.decode('utf-8')
    parsed_body = json.loads(parsed_body)
    parsed_body = parsed_body['data']
    user = User(token=parsed_body["token"], username=parsed_body["username"], photo_url=parsed_body["photo_url"], about_me=parsed_body["about_me"], country=parsed_body["country"])
    user.save()
    parsed_user = serialize('json', [user])
    return HttpResponse(parsed_user, content_type='application/json')

def delete_user_profile(request, token):
    User.objects.filter(token=token).delete()
    return HttpResponse({'Message': "Profile Deleted"})

def get_user_visited(request, token):
    user = User.objects.get(token=token)
    found_user_visited = User_Visit.objects.filter(user=user, visited=True)
    parsed_visits = serialize('json', found_user_visited)
    return HttpResponse(parsed_visits, content_type='application/json')

def get_user_dream_visit(request, token):
    user = User.objects.get(token=token)
    found_user_dream_visit = User_Visit.objects.filter(user=user, dream_visit=True)
    parsed_visits = serialize('json', found_user_dream_visit)
    return HttpResponse(parsed_visits, content_type='application/json')

def user_visited(request, cpk, token):
    user = User.objects.get(token=token)
    country = Country.objects.get(id=cpk)
    found_user_visited = User_Visit.objects.filter(user=user, country=country, visited=True, dream_visit=False)
    if not found_user_visited:
        user_visit = User_Visit(user=user, country=country, visited=True, dream_visit=False)
        user_visit.save()

    else:
        found_user_visited.delete()
        
    parsed_user_visited = serialize('json', [user_visit])
    return HttpResponse(parsed_user_visited, content_type='application/json')


# def user_visited(request, cpk, token):
#     user = User.objects.get(token=token)
#     country = Country.objects.get(id=cpk)
#     found_user_dream_visit = User_Visit.objects.filter(user=user, country=country, visited=True, dream_visit=False)parsed_user_visited