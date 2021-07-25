from django.db import models
from django.contrib.auth.models import User

from trunk.models import EyeKey
# Create your models here.


class Traveler(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, related_name='profile')
    eyekeys = models.ManyToManyField(EyeKey)
