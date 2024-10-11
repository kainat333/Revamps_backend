from django.urls import path 
from .views import Crud ,Del_Patch
urlpatterns=[
    path('',Crud.as_view(),name="crud"),
    path('request/<int:id>/', Del_Patch.as_view(),name="delete patch")
]