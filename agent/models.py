from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# User = get_user_model()
class User(AbstractUser):
   
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    id_number= models.CharField(max_length =30)
    house = models.OneToOneField('House', on_delete=models.CASCADE, null=True)
    house_number= models.CharField(max_length =30)
    phone_number = models.CharField(max_length = 10)
    image = models.ImageField(upload_to='images/')
    post_date = models.DateTimeField(auto_now_add=True)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    tenant = models.BooleanField(default=True)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    
    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()
    
    @classmethod
    def user_profile(cls,id):
        profile = User.objects.get(id=id)
        return profile

class House(models.Model):
    house_choice = [('B', 'B-sitter'), ('1Br', 'One Bedroom'), ('2Br', 'Two Bedroom'),('3Br', 'Three Bedroom')]
    house_type = models.CharField(choices=house_choice,max_length=3,default=None,null=True)
    house_floor = models.CharField(max_length=5,null=True)
    name = models.CharField(max_length=10)
    vacant = models.BooleanField(default=False)
    building = models.ForeignKey('Building', on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.name

    def save_house(self):
        self.save()

class tests(models.Model):
    image=models.ImageField(upload_to="imgs")

class Building(models.Model):
    building_name = models.CharField(max_length =30)
    building_location = models.CharField(max_length =30)
    street = models.CharField(max_length =30)
    plot_number= models.CharField(max_length =30)
   
    

    def __str__(self):
        return self.building_name

    def save_building(self):
        self.save()