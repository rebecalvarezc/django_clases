from django.contrib import admin
from orders.models import Clients, Goods, Orders


# Register your models here.
admin.site.register(Clients)
admin.site.register(Goods)
admin.site.register(Orders)