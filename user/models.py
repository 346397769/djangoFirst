from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    icon = models.ImageField(upload_to='uploads/%Y/%m/%d', verbose_name='用户头像')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
