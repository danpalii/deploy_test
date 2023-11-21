from django.contrib.auth.management.commands import createsuperuser
from decouple import config


class Command(createsuperuser.Command):

    def add_arguments(self, parser):
        parser.add_argument("--user", default=config('SUPER_USER_NAME'))
        parser.add_argument("--password", default=config('SUPER_USER_PASSWORD'))

    def handle(self, *args, **options):
        password = options["password"]
        username = options["user"]
        email = config('SUPER_USER_EMAIL')

        if self.UserModel._default_manager.db_manager().filter(username=username).exists():
            return

        self.UserModel._default_manager.db_manager().create_superuser(password=password, username=username, email=email)