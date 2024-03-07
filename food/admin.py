from django.contrib import admin
from .models import Restaurant

# Register your models here.

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
      list_display = ('restaurant_name', 'restaurant_menu', 'pub_date', 'image')
  