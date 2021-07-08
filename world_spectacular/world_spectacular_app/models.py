from django.db import models

# Create your models here.
class User(models.Model): 
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=150, null=True)
    about_me = models.TextField(max_length=350, null=True)
    country_code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

# class User_Visit(models.Model): 
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visits')
#     country_code = models.CharField(max_length=50, null=True)
#     visited = models.BooleanField(default=False)
#     dream_visit  = models.BooleanField(default=False)

#     def __str__(self):        
#         return (self.user + self.country_code)

# class Country(models.Model): 
#     country = models.CharField(max_length=100, null=False)
#     abbr = models.CharField(max_length=3, null=False) 
#     wiki_name = models.CharField(max_length=150, null=True)
#     anthem = models.CharField(max_length=150, null=True)
#     globe_map = models.CharField(max_length=150, null=True)
#     picture1 = models.CharField(max_length=150, null=True)
#     picture2 = models.CharField(max_length=150, null=True)

#     def __str__(self):        
#         return (self.country + self.abbr)
