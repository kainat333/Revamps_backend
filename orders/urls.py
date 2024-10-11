
from django.urls import path ,include
from .views import Purchase
urlpatterns = [
     path('purchase/', Purchase.as_view(), name='purchase'), 
   
]
