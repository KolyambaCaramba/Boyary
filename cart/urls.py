from django.urls import path
from .views import cart_detail, add_to_cart, cart_remove_product


app_name = 'cart'
urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', cart_remove_product, name='cart_remove_product'),
]