from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('catalog', views.catalog, name='catalog'),
    path('contacts', views.contacts, name='contacts'),
]
