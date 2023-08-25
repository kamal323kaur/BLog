from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name="index"),
      
    path('createpost/',createpost,name="createpost"),
    path('deletepost/<int:id>',deletepost,name="deletepost"),
    path('updatepost/<int:id>',updatepost,name="updatepost"),
    path('registeruser/',registeruser,name="registeruser"),
    path('login/',loginuser,name="login"),
    path('logoutuser/',logoutuser,name="logoutuser"),
    path('post/<int:post_id>/', comment, name='comment'),
    path('comment/<int:comment_id>/like/', like_comment, name='like_comment'),
    
    ]
