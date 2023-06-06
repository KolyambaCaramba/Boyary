from django.shortcuts import render
def about_template(request):
    return render(request, 'about/about.html')

def cart(request):
    return render(request, 'cart/detail_cart.html')

def order(request):
    return render(request, 'orders/order/create.html')