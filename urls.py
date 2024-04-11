from django.contrib import admin
from django.urls import path
from homeapp import views

urlpatterns = [
    #ARTIST_CRUD_API
   path('artists/',views.Artist_create.as_view()),
]
