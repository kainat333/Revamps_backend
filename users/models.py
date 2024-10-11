from django.db import models

class User(models.Model):
    # id = models.CharField(max_length=10, primary_key=True)  # Unique ID for the user
    username = models.CharField(max_length=150, unique=True)  # Unique username
    email = models.EmailField(unique=True)  # Unique email address
    password = models.CharField(max_length=128)  # Hashed password

    def __str__(self):
        return self.username
