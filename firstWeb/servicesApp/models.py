from django.db import models


# Create your models here.
# creamos un mapeo ORM

class Service(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    picture = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

# cuando creamos un modelo podemos especificar características llamadas meta
    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.title