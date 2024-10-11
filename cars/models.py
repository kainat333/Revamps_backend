from django.db import models

# Model for New Cars
class NewCar(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.CharField(max_length=50)  # You can change this to DecimalField if you want to handle numeric prices
    location = models.CharField(max_length=100)
    image = models.CharField(max_length=255)  # Adjust this based on your media settings
    kilometers = models.IntegerField()
    fuelType = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    bodyType = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    engineCapacity = models.IntegerField()
    registeredIn = models.CharField(max_length=4)  # Year as a string, adjust if needed
    is_active = models.BooleanField(default=True)  # New field to indicate active status

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'


# Model for Used Cars
class UsedCar(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    kilometers = models.IntegerField()
    fuelType = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    bodyType = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    engineCapacity = models.IntegerField()
    registeredIn = models.CharField(max_length=4)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'
