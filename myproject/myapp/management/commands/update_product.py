from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Product

class Command(BaseCommand):
    help = "Update product by id."

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Product id")
        parser.add_argument("name", type=str, help="Product name")
        parser.add_argument("description", type=str, help="Product description")
        parser.add_argument("price", type=float, help="Product price")
        parser.add_argument("digits", type=int, help="Product digits")
        
    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        name = kwargs["name"]
        description = kwargs["description"]
        price = kwargs["price"]
        digits = kwargs["digits"]
        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.description = description
        product.price = price
        product.digits = digits
        product.save()
        self.stdout.write(f'{product}')