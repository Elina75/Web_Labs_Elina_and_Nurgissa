from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('aesthetic', views.aesthetic, name='aesthetic'),
    path('birthday', views.birthday, name='birthday'),
    path('kids', views.kids, name='kids'),
    path('wedding', views.wedding, name='wedding'),
    path('corporative', views.corporative, name='corporative'),
    path('registration', views.registration, name='registration'),
    path('all-products', views.products, name='productspage'),
    path('create-a-new-product', views.createproduct, name='createproduct'),
    path('update/<pk>', views.productupdate.as_view(template_name='index/productupdate.html'), name='updateproduct'),
    path('delete/<pk>', views.productdelete.as_view(template_name='index/productdelete.html'), name='deleteproduct'),
    path('product/<id>', views.product, name='productdetails'),
    path('productdetailsbuy/<id>', views.productdetailbuy, name='productdetailbuy')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


