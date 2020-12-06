
from django.urls import path
from .views import Bloglist,Blog_detail

urlpatterns = [
   
    path('bloglist/',Bloglist),
    path('detail/<int:pk>',Blog_detail)
]
