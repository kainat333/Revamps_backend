from django.urls import path, include
from .views import  Save_data
urlpatterns=[
path('save-contact-data/',Save_data.as_view(),name="save-data")
]