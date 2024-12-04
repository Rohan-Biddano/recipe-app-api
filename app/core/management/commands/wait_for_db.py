"""
Django Command to wait for the databse to be available.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """"Django commnad to wait for the databse to be available"""

    def handle(self, *args, **options):
        pass