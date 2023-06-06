from django.db import models
from products.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    
    email = models.EmailField()
    street = models.CharField(max_length=100,blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=True, null=True)
    building_number = models.CharField(max_length=10, blank=True, null=True)
    apartment_office_number = models.CharField(max_length=10, blank=True, null=True)
    entrance_number = models.CharField(max_length=10, blank=True, null=True)
    floor_number = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    
    additional_notes = models.CharField(max_length=200, blank=True, null=True)
    privacy_policy = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    paid = models.BooleanField(default=False) # поле для различения оплаченных и неоплаченных заказов

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)
    """общая стоимость товаров
    """
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    """
    хранение продукт, количество и цену, уплаченную за каждый товар
    """

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,  related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
    """
    возврата стоимости товара
    """

    def get_cost(self):
        return self.price * self.quantity 