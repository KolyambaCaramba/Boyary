# импорт модуля models из библиотеки django.db
from django.db import models
# импорт модели Product из приложения products
from products.models import Product
 # создание модели Order
class Order(models.Model):
    # поля модели
    first_name = models.CharField(max_length=50) # имя
    last_name = models.CharField(max_length=50) # фамилия
    middle_name = models.CharField(max_length=100, blank=True, null=True) # отчество
    email = models.EmailField() # электронная почта
    street = models.CharField(max_length=100,blank=True, null=True) # улица
    house_number = models.CharField(max_length=10, blank=True, null=True) # номер дома
    building_number = models.CharField(max_length=10, blank=True, null=True) # номер корпуса
    apartment_office_number = models.CharField(max_length=10, blank=True, null=True) # номер квартиры/офиса
    entrance_number = models.CharField(max_length=10, blank=True, null=True) # номер подъезда
    floor_number = models.CharField(max_length=10, blank=True, null=True) # номер этажа
    phone_number = models.CharField(max_length=20, blank=True, null=True) # номер телефона
    additional_notes = models.CharField(max_length=200, blank=True, null=True) # дополнительные заметки
    privacy_policy = models.BooleanField(default=False) # политика конфиденциальности
    created = models.DateTimeField(auto_now_add=True) # дата создания заказа
    paid = models.BooleanField(default=False) # поле для различения оплаченных и неоплаченных заказов
     # метаданные модели
    class Meta:
        ordering = ('-created',) # сортировка заказов по дате создания в обратном порядке
        verbose_name = 'Заказ' # имя модели в единственном числе
        verbose_name_plural = 'Заказы' # имя модели во множественном числе
     # метод для вывода названия заказа
    def __str__(self):
        return 'Order {}'.format(self.id)
     # метод для получения общей стоимости товаров в заказе
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
 # создание модели OrderItem
class OrderItem(models.Model):
    # поля модели
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,  related_name='items') # связь с моделью Order
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='order_items') # связь с моделью Product
    price = models.DecimalField(max_digits=10, decimal_places=2) # цена товара
    quantity = models.PositiveIntegerField(default=1) # количество товара
     # метод для вывода названия заказа
    def __str__(self):
        return '{}'.format(self.id)
     # метод для получения стоимости товара
    def get_cost(self):
        return self.price * self.quantity