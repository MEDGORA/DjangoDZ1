from django.core.management.base import BaseCommand, CommandParser
from myapp.models import Order

class Command(BaseCommand):
    help = "Get order by id."

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Order id")

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')