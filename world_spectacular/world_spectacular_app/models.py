from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Country(models.Model): 
    country_name = models.CharField(max_length=100, null=False)
    country_code = models.CharField(max_length=3, null=False, unique=True) 
    wiki_link = models.CharField(max_length=500, default=None)
    anthem = models.CharField(max_length=500, blank=True, default=None)
    globe_map = models.CharField(max_length=500, default=None)

    def __str__(self):        
        return (self.country_name + ' - ' + self.country_code)
        # return (int(self.id))
    # def slug(self):
    #     return (slugify(self.country_code))

class Country_Picture(models.Model): 
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='pictures')
    picture_url = models.CharField(max_length=1500, null=False)
    picture_location = models.CharField(max_length=500, null=False)
    picture_photographer = models.CharField(max_length=500, default=None)
    picture_photographer_link = models.CharField(max_length=1500, default=None)
    picture_source = models.CharField(max_length=1500, default=None)

    def __str__(self):        
        return (str(self.country) + ' - ' + self.picture_location)

class User(models.Model): 
    token = models.CharField(max_length=150)
    username = models.CharField(max_length=50, null=False)
    photo_url = models.CharField(max_length=150, null=True, blank=True)
    about_me = models.TextField(max_length=350, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name='user', null=True, blank=True)

    def __str__(self):
        return self.username

class User_Visit(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_visit')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='user_country_visit')
    visited = models.BooleanField(default=False)
    dream_visit  = models.BooleanField(default=False)

    def __str__(self):        
        return (self.user_id + self.country_id)