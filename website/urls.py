from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario', views.usuario, name='usuario'),
    path('accounts/', include('django.contrib.auth.urls')),
]