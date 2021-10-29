from django.urls import path
from views import home, services, store, contact_us, blog

urlpatterns = [
    path('', home, name='home'),
    path('services', services, name='services'),
    path('store', store, name='store'),
    path('us', contact_us, name='contact'),
    path('blog', blog, name='blog'),
]
