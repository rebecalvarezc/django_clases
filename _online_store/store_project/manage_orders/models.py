from django.db import models


# Create your models here.
# El código SQL lo crea Django por detrás.

class Clients(models.Model):
    name = models.CharField(max_length=30)  # de tipo texto.
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)


class Goods(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return f'The article name is {self.name}, the section is {self.section} and the price is {self.price}$.'


class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()
