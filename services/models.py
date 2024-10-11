from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)  # Title of the service
    description = models.TextField()  # Description of the service

    def __str__(self):
        return self.title


class Submission(models.Model):
    # id = models.CharField(max_length=10, primary_key=True)  # Unique ID for the submission
    name = models.CharField(max_length=100)  # Name of the submitter
    email = models.EmailField()  # Email address
    address = models.CharField(max_length=255)  # Address of the submitter
    tel = models.BigIntegerField(null=True, blank=True)  # Telephone number (optional)
    postcode = models.CharField(max_length=20)  # Postcode
    ServeYouWant = models.TextField()  # Description of the service wanted

    def __str__(self):
        return f'Submission from {self.name}'
