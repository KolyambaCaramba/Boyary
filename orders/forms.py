from django import forms
from .models import Order


# class OrderCreateForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

class OrderCreateForm(forms.ModelForm):
    
    
    last_name = forms.CharField(label='Фамилия', max_length=100)
    first_name = forms.CharField(label='Имя', max_length=100)
    middle_name = forms.CharField(label='Отчество', max_length=100)
    street = forms.CharField(label='Улица', max_length=100)
    house_number = forms.CharField(label='Дом', max_length=10)
    building_number = forms.CharField(label='Корпус', max_length=10, required=False)
    apartment_office_number = forms.CharField(label='Квартира/офис', max_length=10)
    entrance_number = forms.CharField(label='Подъезд', max_length=10, required=False)
    floor_number = forms.CharField(label='Этаж', max_length=10, required=False)
    phone_number = forms.CharField(label='Контактный номер телефона', max_length=20)
    email = forms.EmailField(label='Е-майл')
    payment_method = forms.ChoiceField(label='Выбор способа оплаты', choices=[('cash', 'Наличный'), ('non_cash', 'Безналичный')])
    additional_notes = forms.CharField(label='Доп. заметки', widget=forms.Textarea(attrs={'rows': 3}))
    privacy_policy = forms.BooleanField(label='Я прочитал и согласен с политикой конфиденциальности')

    class Meta:
        model = Order
        fields = ['last_name', 'first_name', 'middle_name', 'street', 'house_number',
                  'building_number', 'apartment_office_number', 'entrance_number', 'floor_number', 'phone_number',
                  'email', 'payment_method', 'additional_notes', 'privacy_policy']