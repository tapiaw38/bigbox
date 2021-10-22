from django.contrib import admin
from django.contrib.admin.decorators import register

# Models 
from bigbox.core.models import (
  
    Box,
    BoxImage,
    Activity,
    ActivityImage,
    Category,
    Reason
)

# Register your models here.

@admin.register(Box)
class Box(admin.ModelAdmin): 
    pass

@admin.register(BoxImage)
class BoxImage(admin.ModelAdmin): 
    pass

@admin.register(Activity)
class Activity(admin.ModelAdmin): 
    pass

@admin.register(ActivityImage)
class ActivityImage(admin.ModelAdmin): 
    pass

@admin.register(Category)
class Category(admin.ModelAdmin): 
    pass


@admin.register(Reason)
class Reason(admin.ModelAdmin): 
    pass
