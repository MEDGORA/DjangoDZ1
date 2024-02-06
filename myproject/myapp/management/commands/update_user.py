from django.core.management.base import BaseCommand, CommandParser
from myapp.models import User

class Command(BaseCommand):
    help = "Update user by id."

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User id")
        parser.add_argument("name", type=str, help="User name")
        parser.add_argument("email", type=str, help="User email")
        parser.add_argument("phone", type=str, help="User phone")
        parser.add_argument("adress", type=str, help="User adress")

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        name = kwargs["name"]
        email = kwargs["email"]
        phone = kwargs["phone"]
        adress = kwargs["adress"]
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.email = email
        user.phone = phone
        user.adress = adress
        user.save()
        self.stdout.write(f'{user}')