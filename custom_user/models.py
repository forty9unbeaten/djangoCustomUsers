from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyCustomUser(AbstractUser):
    homepage = models.URLField()
    display_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
