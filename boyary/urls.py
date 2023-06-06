from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('about', views.about_template, name='about_template'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('', include('products.urls', namespace='products')),
    path('admin', admin.site.urls),
    path('politica', include('politica.urls', namespace='politica')),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)