from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=100,unique = True)
    email = models.EmailField()
    DOB = models.DateField()

    def __str__(self):
        return f"{self.username}-{self.name}"