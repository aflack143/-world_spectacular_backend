from django.db import models

# Create your models here.
class Country(models.Model): 
    country_name = models.CharField(max_length=100, null=False)
    country_code = models.CharField(max_length=3, null=False) 
    wiki_link = models.CharField(max_length=500, null=True)
    anthem = models.CharField(max_length=500, null=True)
    globe_map = models.CharField(max_length=500, null=True)

    def __str__(self):        
        return (self.country_name + self.country_code)

class Country_Picture(models.Model): 
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='pictures')
    picture_url = models.CharField(max_length=500, null=False)
    picture_location = models.CharField(max_length=150, null=False)
    picture_photographer = models.CharField(max_length=150, null=True)
    picture_photographer_link = models.CharField(max_length=500, null=True)
    picture_source = models.CharField(max_length=500, null=True)

    def __str__(self):        
        return (self.country_id)

class User(models.Model): 
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50, null=False)
    token = models.CharField(max_length=150)
    photo_url = models.CharField(max_length=150)
    about_me = models.TextField(max_length=350, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name='user', null=True)

    def __str__(self):
        return self.email

class User_Visit(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_visit')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='user_country_visit')
    visited = models.BooleanField(default=False)
    dream_visit  = models.BooleanField(default=False)

    def __str__(self):        
        return (self.user_id + self.country_id)