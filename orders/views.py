from django.shortcuts import render
from .models import OrderItem 
from .forms import OrderCreateForm
from cart.cart import Cart
# from .tasks import order_created
# from utils.emails import SendingEmail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            #  data = {
            #      'first_name': form.cleaned_data['first_name'],
            #      'first_name': form.cleaned_data['first_name'],
            #      'email':  form.cleaned_data['first_name']
            #  }
            # html_body = render_to_string('emals_templates/order_admin.html', data)
            # msg = EmailMultiAlternatives(subject='sdffghhfggg', to=['krivov.av91@yandex.ru'])
            # msg.attach_alternative(html_body, 'text/html')
            # msg.send()
            
            
            order = form.save()

            for item in cart:
                 OrderItem.objects.create(order=order,
                                          product=item['product'],
                                          price=item['price'],
                                           quantity=item['quantity'])
           
            context = {

                 
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                
                'middle_name': form.cleaned_data['middle_name'],
                'street': form.cleaned_data['street'],
                'house_number': form.cleaned_data['house_number'],
                'building_number': form.cleaned_data['building_number'],
                'apartment_office_number': form.cleaned_data['apartment_office_number'],
                'entrance_number': form.cleaned_data['entrance_number'],
                'floor_number': form.cleaned_data['floor_number'],
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'payment_method': form.cleaned_data['payment_method'],
                'additional_notes':form.cleaned_data['additional_notes'],
                
                'cart': cart
                
             }
            
            html_body = render_to_string('emals_templates/order_admin.html', context)
            msg = EmailMultiAlternatives(subject='Новый заказ', to=['krivov.av91@yandex.ru'])
            msg.attach_alternative(html_body, 'text/html')
            msg.send()
            # # очистка корзины
            # # email = SendingEmail()
            # # email.sending_email(type_id=1, order=order)
            cart.clear()
            
            # email.sending_email(type_id=2, order=order) 
            
# # запуск асинхронной задачи
#             order_created.delay(order.id)
            return render(request, 'orders/order/created.html'
                         )
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})   
