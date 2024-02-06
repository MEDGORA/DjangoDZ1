from django.core.management.base import BaseCommand
from myapp.models import Order

class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        order = Order(customer=["Павел","123@mail.ru", "88005353535" ,"г. Москва"], products=[["Картошка", "Просто картошка", "60" , "12"]], 
                      total_price="60")
        order.save()
        self.stdout.write(f'{order}')