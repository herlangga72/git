from django.contrib.auth.models import AbstractUser
from django.db import models


# add column what you want to add to user class this is extended user class in django

class User(AbstractUser):
    is_pekerti_peserta = models.BooleanField("Apakah Peserta Pekerti",default=False)
    avatar = models.CharField(max_length=255,blank=True)