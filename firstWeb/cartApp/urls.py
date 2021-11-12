from django.urls import path
from .views import add_product, delete_product, delete_cart, remove_product

app_name = 'cart'
# para evitar problemas con los nombres dados a las urls

urlpatterns = [
    path('add/<int:product_id>/', add_product, name='add'),
    path('delete/<int:product_id>/', delete_product, name='delete'),
    path('remove/<int:product_id>/', remove_product, name='remove'),
    path('clear/', delete_cart, name='clear'),
]
