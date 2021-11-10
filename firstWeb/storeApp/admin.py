from django.contrib import admin
from .models import ProdCat, Product


# Register your models here.
class ProdCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(ProdCat, ProdCategoryAdmin)
admin.site.register(Product, ProductAdmin)
