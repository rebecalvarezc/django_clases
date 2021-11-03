from django.urls import path
from webProject.views import home, store, contact_us
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('store', store, name='store'),
    path('us', contact_us, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
