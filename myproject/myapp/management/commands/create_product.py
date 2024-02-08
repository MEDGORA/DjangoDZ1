from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name="Шоколадка", description ="Просто шоколадка", price="40" , digits="1")
        product.save()
        self.stdout.write(f'{product}')