from django.urls import path
from my_app import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('user',views.user),
    path('search',views.search),
    path('login',views.login),
    path('register',views.register),
    path('contact', views.contact),
    path('result', views.result),
    path('dairy', views.dairy),
    path('read', views.read),
    path('add', views.add)

    path('external_api', views.external_api),
    path('pincode', views.pincode),
]