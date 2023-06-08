from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
def send_order_email(order, cart):
    context = {
        'first_name': order.first_name,
        'last_name': order.last_name,
        'middle_name': order.middle_name,
        'street': order.street,
        'house_number': order.house_number,
        'building_number': order.building_number,
        'apartment_office_number': order.apartment_office_number,
        'entrance_number': order.entrance_number,
        'floor_number': order.floor_number,
        'phone_number': order.phone_number,
        'email': order.email,
        'payment_method': order.payment_method,
        'additional_notes': order.additional_notes,
        'cart': cart
    }
    html_body = render_to_string('emals_templates/order_admin.html', context)
    msg = EmailMultiAlternatives(subject='Новый заказ', to=['krivov.av91@yandex.ru'])
    msg.attach_alternative(html_body, 'text/html')
    msg.send()
def order_create(request):
    cart = Cart(request)пше
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            send_order_email(order, cart)
            cart.clear()
            return render(request, 'orders/order/created.html')
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})