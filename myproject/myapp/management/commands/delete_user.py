from django.core.management.base import BaseCommand, CommandParser
from myapp.models import User

class Command(BaseCommand):
    help = "Delete user by id."

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User id")

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')