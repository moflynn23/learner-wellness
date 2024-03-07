from django.urls import include, path
from . import views
from django.contrib import admin


urlpatterns = [
    path("", views.food, name="food"),
#   path("polls/", include("polls.urls")),   # sample - access other apps in the project
#    path("admin/", admin.site.urls),
]

# The include() function allows referencing other URLconfs. 
# Whenever Django encounters include(), it chops off whatever part of the URL matched up 
# to that point and sends the remaining string to the included URLconf 
# for further processing.
