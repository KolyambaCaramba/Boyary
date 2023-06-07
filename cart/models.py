from django.db import models
from django.conf import settings
from products.models import Product
 # Модель корзины для хранения товаров, выбранных пользователем
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
     # Функция для получения общей стоимости товаров в корзине
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None
        self.items = None

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
     # Функция для получения количества товаров в корзине
    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())
     # Функция для добавления товара в корзину
    def add_to_cart(self, product, quantity=1):
        # Проверяем, есть ли уже такой товар в корзине
        for item in self.items.all():
            if item.product.id == product.id:
                item.quantity += quantity
                item.save()
                return
         # Если товара еще нет в корзине, создаем новый объект CartItem
        cart_item = CartItem(cart=self, product=product, quantity=quantity)
        cart_item.save()
    def __str__(self):
        return f'Корзина {self.id}'
 # Модель для хранения товаров в корзине
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
     # Функция для получения стоимости товара
    def get_cost(self):
        return self.product.price * self.quantity
    def __str__(self):
        return f'{self.product.name} ({self.quantity})'