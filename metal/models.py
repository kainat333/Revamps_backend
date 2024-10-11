from django.db import models

# Create your models here.
class Metal(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    def ___str___(self):
        return self.name
