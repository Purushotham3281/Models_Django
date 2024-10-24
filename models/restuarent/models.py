from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    Quantity=models.CharField(max_length=10)
    



    def __str__(self):
        return self.name