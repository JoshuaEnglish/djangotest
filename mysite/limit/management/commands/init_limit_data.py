"""Initialize Data for the Limit app"""

from django.core.management.base import BaseCommand, CommandError

from limit.models import Role, Person, Team


class Command(BaseCommand):
    help = "Resets the database with testing data"
    
    def handle(self, *args, **kwargs):
        Team.objects.all().delete()
        Person.objects.all().delete()
        Role.objects.all().delete()

        m = Role.objects.create(name='Manager')
        s = Role.objects.create(name='Sales Rep')
        e = Role.objects.create(name='Engineer')

        Person.objects.create(name='Bill', role=m)
        Person.objects.create(name='Sally', role=s)
        Person.objects.create(name='Steven', role=s)
        Person.objects.create(name='Eric', role=e)
        Person.objects.create(name='Edward', role=e)


    
