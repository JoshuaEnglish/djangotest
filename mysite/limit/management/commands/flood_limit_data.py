"""Flood Data for the Limit app, add a hundred users or so"""

from django.core.management.base import BaseCommand, CommandError

from limit.models import Role, Person, Team


class Command(BaseCommand):
    help = "Resets the database with testing data"

    def handle(self, *args, **kwargs):

        s = Role.objects.get(name="Sales Rep")
        e = Role.objects.get(name="Engineer")

        for idx in range(1, 50):
            Person.objects.create(name=f"S_{idx:02}", role=s)
            Person.objects.create(name=f"E_{idx:02}", role=e)
