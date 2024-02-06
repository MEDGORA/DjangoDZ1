from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    adress = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Имя: {self.name}, почта: {self.email}, телефон: {self.phone}, адресс: {self.adress}, дата регистрации: {self.date_created}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    digits = models.IntegerField()
    date_product_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Название: {self.name}, описание: {self.description}, цена: {self.price}, количество: {self.digits}, дата добавления: {self.date_product_added}"

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказчик: {self.customer}, продукты: {self.products}, общая стоимость: {self.total_price}, дата заказа: {self.date_ordered}"