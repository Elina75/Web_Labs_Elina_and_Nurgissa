from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('aesthetic', views.aesthetic, name='aesthetic'),
    path('birthday', views.birthday, name='birthday'),
    path('kids', views.kids, name='kids'),
    path('wedding', views.wedding, name='wedding'),
    path('corporative', views.corporative, name='corporative'),

]
