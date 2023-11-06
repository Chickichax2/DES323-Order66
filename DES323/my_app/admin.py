from django.contrib import admin
from .models import *

@admin.register(dairy_dataset)
class dairy_dataset(admin.ModelAdmin):
    pass

@admin.register(user)
class user(admin.ModelAdmin):
    pass



