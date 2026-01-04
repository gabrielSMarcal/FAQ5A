from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faq/', include('faq.urls')),
    path('colinha/', include('colinha.urls')),
]
