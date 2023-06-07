from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'boyary'
urlpatterns = [
    path('about', views.about_template, name='about_template'),
    path('instruction', views.instruction, name='about_template'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('products.urls', namespace='products')),
    path('admin', admin.site.urls),
    path('politica', include('politica.urls', namespace='politica')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)