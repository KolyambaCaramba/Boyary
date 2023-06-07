from django.contrib import admin
from django.urls import path

from . import views


app_name = 'products'
urlpatterns = [    
    path('', views.index, name='index'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='cart_add'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('podcategory/<slug:slug>/', views.podcategory, name='podcategory'),
    path('product/<slug:slug>/',views.product, name='product'),

    
#    path('(?P<category_slug>[-\w]+)/$',
#        views.index,
#        name='product_list_by_category'),
#    path('category/<slug:slug>/', views.index, name='category'),
#    path('(?P<id>\d+)/(?P<slug>[-\w]+)/$',
#        views.product_detail,
#        name='product_detail'),
]    

