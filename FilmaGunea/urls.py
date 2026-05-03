from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.hasiera, name='hasiera'),
    path('login', views.LoginForm.as_view(), name='login'),
    path('register',views.register, name='register'),
    path('sartuta', views.sartuta, name='sartuta'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('create', views.datuBase, name='create'),
    path('katalogoa',views.filmak_ikusi, name="katalogoa"),
    path('bozkatu',views.bozkatu, name="bozkatu"),
    path('zaleak',views.zaleak_ikusi, name="zaleak"),
    path('ezabatu', views.ezabatuDena, name="ezabatu")
]