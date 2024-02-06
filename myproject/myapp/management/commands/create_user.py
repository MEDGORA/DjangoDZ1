from django.core.management.base import BaseCommand
from myapp.models import User

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name="Павел", email ="123@mail.ru", phone="88005353535" , adress="г. Москва")
        user.save()
        self.stdout.write(f'{user}')
