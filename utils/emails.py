# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string, get_template
# from boyary.settings import FROM_EMAIL, EMAIL_ADMIN
# from django.forms.models import model_to_dict
# from emails.models import EmailSedingFact


# class SendingEmail(object):
#     from_email = FROM_EMAIL
#     reply_to_eails= [from_email]
#     target_emails = []
#     bcc_emails = []


#     def sending_email(self, type_id, email=None, order=None):
#         if not email:
#             email = EMAIL_ADMIN
#         target_emails = [email]

#         vars = {

#         }

#         if type_id ==1:
#             subject = 'Новый заказ'
#             vars['order_fields']= model_to_dict(order)
#             vars['order'] = order
#             print(f'смори тут{order}')
#             # vars['products_in_orders'] = order.productinorder_set.filter(is_active=True)
#             massege = get_template('emals_templates/order_admin.html').render(vars)

#         elif  type_id ==2:
#             subject = 'мы поучили заказ'
#             massege = get_template('emals_templates/order_client.html').render(vars)


#         msg = EmailMessage(
#             subject, massege, from_email=self.from_email, to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_eails)
        
#         msg.content_subtype = 'html'
#         msg.mixed_subtype = 'related'
       
#         msg.send()


#         kwargs = {
#              'type_id': type_id,
#              'email':email
#         }
#         # if order:
#         #     kwargs['order'] = order

#         print(f'смотри тут:{kwargs}')
#         EmailSedingFact.objects.create(**kwargs)
       


#         #     print('Email fuck')







