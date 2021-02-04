from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Product(models.Model):
    MOBILE = 'Mobile'
    LAPTOP = 'Laptop'
    
    CHOICES = [
        (MOBILE, 'Mobile'),
        (LAPTOP, 'Laptop'),
        
    ]

    name = models.TextField()
    description = models.TextField()
    type = models.CharField(max_length=15,choices=CHOICES,default='')
    processor = models.CharField(max_length=250)
    ram = models.CharField(max_length=250,default='')
    screen_size = models.CharField(max_length=200,default='')
    color = models.CharField(max_length=250,default='')
    hd_capacity = models.CharField(max_length=200,default='')
    