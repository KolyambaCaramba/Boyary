from django.shortcuts import render
def about_template(request):
    return render(request, 'about/about.html')
def cart(request):
    return render(request, 'cart/detail_cart.html')
def order(request):
    return render(request, 'orders/order/create.html')
def order_create(request):
    return render(request, 'order_create.html')
def instruction(request):
    return render(request, 'instruction.html')
