from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator
# Create your models here.
class Advert (models.Model):
    business_name = models.CharField(max_length=254, default='')
    info = models.TextField(default='')
    contact_email = models.EmailField()
    contact_telephone = models.CharField(max_length=254, default='')
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE )
    slug = models.SlugField(max_length=50)
    category = models.CharField(max_length=254, default='')
    advert_image = models.ImageField(upload_to='media/adverts')
    header_image = models.ImageField(upload_to='media/images')
    website = models.CharField(max_length=254, default='')
    
    
    def __str__(self):
        return self.business_name 
        
class Category (models.Model):
    category_name = models.CharField(max_length=254, default='')
    def __str__(self):
        return self.category_name 