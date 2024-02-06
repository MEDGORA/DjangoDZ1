from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name="Картошка", description ="Просто картошка", price="60" , digits="12")
        product.save()
        self.stdout.write(f'{product}')