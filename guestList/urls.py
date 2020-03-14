from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('convidados/', include('convidado.urls')),
    path('eventos/', include('evento.urls')),
    path('', include('django.contrib.auth.urls')),
]
