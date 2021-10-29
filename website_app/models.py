from django.db import models
from django.db.models.fields import IntegerField
from django import forms

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    username = models.CharField(max_length=250, blank=True, null=True, default='name')
    email = models.CharField(max_length=250, blank=False, null=False)

def __str__(self):
        return self.username



class Category(models.Model):
    HOME = 'HM'
    PETS = 'PT'
    CAR = 'CR'
    ELECTRONICS = 'EL'
    HOBBIES = 'HB'
    CATEGORYCHOICES = [
        (HOME, 'Home'),
        (PETS, 'Pets'),
        (CAR, 'Car'),
        (ELECTRONICS, 'Electronics'),
        (HOBBIES, 'Hobbies'),
    ]
    category_choice = models.CharField(
        max_length=2,
        choices=CATEGORYCHOICES,
        default=HOBBIES,
    )
    # def __str__(self):
    #     return self.
    def is_category_choice(self):
        return self.username

    # def user_directory_path(instance, images):
class Products(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False, default='none')
    tagline = models.CharField(max_length=250, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    description = models.CharField(max_length=250, null=True, blank=False)
    product_image = models.ImageField(null=True, blank=True, upload_to='images/')
    
    def __str__(self):
        return self.name