from django.contrib import admin

# Register your models here.
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name')
    # fields = ['username', 'first_name', 'last_name']


admin.site.register(User, UserAdmin)
