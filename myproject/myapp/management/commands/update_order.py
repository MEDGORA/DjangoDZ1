from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Order

class Command(BaseCommand):
    help = "Update order by id."

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Order id")
        parser.add_argument("customer", type=list, help="customer")
        parser.add_argument("products", type=list, help="products")
        parser.add_argument("total_price", type=float, help="total price")

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        customer = kwargs["customer"]
        products = kwargs["products"]
        total_price = kwargs["total_price"]
        order = Order.objects.filter(pk=pk).first()
        order.customer = customer
        order.products = products
        order.total_price = total_price
        order.save()
        self.stdout.write(f'{order}')