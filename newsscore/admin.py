from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import CustomUser

admin.site.register(User)

# If using a custom user model
admin.site.register(CustomUser)