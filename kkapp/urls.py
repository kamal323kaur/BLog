from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name="index"),
    path('nextt/',nextt,name="nextt"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),    
    path('post/',post,name="post"),
    path('createpost/',createpost,name="createpost"),
    path('deletepost/<int:id>',deletepost,name="deletepost"),
    path('updatepost/<int:id>',updatepost,name="updatepost"),
    path('registeruser/',registeruser,name="registeruser"),
    path('login/',loginuser,name="login"),
    path('logoutuser/',logoutuser,name="logoutuser"),
    ]
