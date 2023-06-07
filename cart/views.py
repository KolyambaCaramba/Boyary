from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cart.cart import Cart
from products.models import Product
from .forms import CartAddProductForm
 # декоратор, который проверяет, что запрос был отправлен методом POST
@require_POST
def add_to_cart(request, product_id):
    cart_obj = Cart(request)  # создание экземпляра корзины
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart_obj.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart001.html')  # изменено на правильное имя URL
 # функция для отображения содержимого корзины
def cart_detail(request):
    cart_obj = Cart(request)
    return render(request, 'cart001.html', {'cart': cart_obj})
 # функция для очистки корзины
def cart_remove(request):
    cart_obj = Cart(request)
    cart_obj.clear()
    return redirect('cart001.html')  # изменено на правильное имя URL
 # функция для удаления одного товара из корзины
def cart_remove_product(request, product_id):
    cart_obj = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_obj.remove(product)
    return redirect('cart001.html')  # изменено на правильное имя URL