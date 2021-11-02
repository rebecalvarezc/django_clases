from django.contrib import admin
from .models import Categories, Post


# Register your models here.
class CatAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Categories, CatAdmin)
admin.site.register(Post, PostAdmin)
