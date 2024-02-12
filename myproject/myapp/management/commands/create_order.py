from django.core.management.base import BaseCommand
from myapp.models import Order, User, Product

class Command(BaseCommand):
    help = "Create order."

    """
    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User id")

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
    """

    def handle(self, *args, **kwargs):
        order = Order(customer=User.objects.filter(pk="1").first(), products=set([Product.objects.filter(pk="1").first(), Product.objects.filter(pk="3").first()]), 
                      total_price="60")
        order.save()
        self.stdout.write(f'{order}')