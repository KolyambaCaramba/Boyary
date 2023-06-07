from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
 # декоратор, который проверяет, что запрос был отправлен методом POST
@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)  # создание экземпляра корзины
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')
 # функция для отображения содержимого корзины
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
 # функция для очистки корзины
def cart_remove(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')
 # функция для удаления одного товара из корзины
def cart_remove_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove_single(product)
    return redirect('cart:cart_detail')