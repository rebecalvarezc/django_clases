from django.urls import path
from .views import contact_us


urlpatterns = [
    path('us', contact_us, name='contact'),
]

