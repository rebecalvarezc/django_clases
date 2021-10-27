from django.contrib import admin
from orders.models import Clients, Goods, Orders


# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'phone')


class GoodsAdmin(admin.ModelAdmin):
    list_filter = ('section',)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'delivered')
    list_filter = ('date',)
    date_hierarchy = 'date'


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Orders, OrdersAdmin)
