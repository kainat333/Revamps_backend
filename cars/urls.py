
from django.urls import path ,include
from .views import Cars ,Usedcars,fetch_specific_cars,fetch_specific_used_cars
urlpatterns = [
     path('save-new-car/', Cars.as_view(), name='SaveNewCar'), 
     # path('save-new-cars/', views.post_cars, name='saveCars'),
     path('save-used-car/', Usedcars.as_view(), name='SaveNewCar'),  
     path('fetch-specific-car/<int:id>/', fetch_specific_cars.as_view(), name='fetch_specific_car'),
     path('fetch-specific-used-car/<int:id>/', fetch_specific_used_cars.as_view(), name='fetch_specific_used_car'),
]
