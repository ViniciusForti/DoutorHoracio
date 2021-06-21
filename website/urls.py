from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario', views.usuario, name='usuario'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('logout', views.logoutView, name='logout'),
    path('cadastrar_usuario', views.cadastrar_usuario, name='cadastrar_usuario'),

    path('password_reset_complete', views.password_reset_complete, name='password_reset_complete'),
    path('password_reset_confirm', views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_done', views.password_reset_done, name='password_reset_done'),
    path('password_reset_form', views.password_reset_form, name='password_reset_form'),
]