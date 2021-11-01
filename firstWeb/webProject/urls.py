from django.urls import path
from webProject.views import home, services, store, contact_us, blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('services', services, name='services'),
    path('store', store, name='store'),
    path('us', contact_us, name='contact'),
    path('blog', blog, name='blog'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)