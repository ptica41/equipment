from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('digis/', include('DIGIS.urls')),
    path('intellect/', include('INTELLECT.urls')),
    path('svetoch/', include('SVETOCH.urls')),
    path('poznaykino/', include('POZNAYKINO.urls')),
]
