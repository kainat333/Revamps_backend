from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=False)
    message = models.TextField()

    def ___str___(self):
        return self.name
