from django.db import models

class Purchase(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
    ]

    id = models.CharField(max_length=10, primary_key=True)  # Use a unique ID for the primary key
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    price = models.CharField(max_length=15)  # Adjust based on your needs
    car_type = models.CharField(max_length=10, blank=True, null=True)  # Optional field
    car_id = models.CharField(max_length=10, blank=True, null=True)  # Optional field

    def __str__(self):
        return f'{self.name} - {self.price}'
