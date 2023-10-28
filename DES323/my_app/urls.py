from django.urls import path
from my_app import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('user',views.user),
    path('search',views.search),
]