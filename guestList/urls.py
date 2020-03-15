from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views


urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('convidados/', include('convidado.urls')),
    path('eventos/', include('evento.urls')),
]
