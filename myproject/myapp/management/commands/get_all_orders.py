from django.core.management.base import BaseCommand
from myapp.models import Order

class Command(BaseCommand):
    help = "Get all orders."

    def handle(self, *args, **kwargs):
        odrers = Order.objects.all()
        self.stdout.write(f'{odrers}')