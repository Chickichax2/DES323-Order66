from django.urls import path
from my_app import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('user',views.user),
    path('search',views.search),
    path('home',views.home),
    path('login',views.login),
    path('logout', views.logout),
    path('register',views.register),
    path('contact', views.contact),
    path('result', views.result),
    # Do not use this path again path('dairy', views.dairy),
    # path('create', views.create),
    # path('read', views.read),
    # path('update', views.update),
    # path('delete', views.delete),
    path('view_user', views.data_sci_item_list_all),
    path('edit/<id>',views.data_sci_item_edit),
    path('delete/<id>',views.data_sci_item_delete),
    path('external_api', views.external_api),
    path('pincode', views.pincode),
    path("api/json/v1/register", views.api_register),
    
]