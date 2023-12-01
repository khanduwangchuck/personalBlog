import uuid

from django.db import models
from  django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField
    username =models.CharField(max_length=20)
    profession= models.CharField(max_length=500)
    picture = models.ImageField(upload_to='img',blank= True, null=True)
    about =models.CharField(max_length=300)
    profile_id = models.UUIDField(default=uuid.uuid4(), editable=False,unique=True,primary_key=True)

    def __str__(self):
        return self.username


