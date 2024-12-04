"""
Django Command to wait for the databse to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    """"Django commnad to wait for the databse to be available"""

    def handle(self, *args, **options):
        """" Entrypoint for command."""
        self.stdout.write('waiting for database')
        db_up= False
        while db_up is False:
            try:
                self.check(databases= ['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('database is not available, waiting 1 seconds...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is available!'))

