from datetime import datetime

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=12, unique=True, null=False, error_messages={'unique': '用户名必须唯一'})
    password = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=11, default="")
    is_delete = models.BooleanField(default=False)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
