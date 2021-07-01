from django.db import models

# Create your models here.
class User(models.Model): 
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=150, null=True)
    about_me = models.TextField(max_length=350, null=True)
    country = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

# class User_Visit(models.Model): 
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visits')
#     visited = models.BooleanField(default=False)
#     dream_visit  = models.BooleanField(default=False)