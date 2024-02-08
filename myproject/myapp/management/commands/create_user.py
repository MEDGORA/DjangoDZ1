from django.core.management.base import BaseCommand
from myapp.models import User

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name="Иван", email ="123456@mail.ru", phone="8800222222" , adress="г. Санкт-Петербург")
        user.save()
        self.stdout.write(f'{user}')
