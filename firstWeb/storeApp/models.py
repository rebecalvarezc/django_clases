from django.db import models


# Create your models here.
class ProdCat(models.Model):
    cat_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'productCategory'
        verbose_name_plural = 'productCategories'

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(ProdCat, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='store', null=True, blank=True)
    # necesario tener instalado Pillow para no tener errores con la migración
    price = models.FloatField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
