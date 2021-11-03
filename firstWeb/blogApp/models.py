from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to='blog', null=True, blank=True)
    # para que la imagen quede en blanco
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # eliminación en cascada
    categories = models.ManyToManyField(Categories)
    # especificamos la relación entre los post y las categorías.
    # Un post puede contener muchas categorías y una categoría puede contener muchos posts.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title
