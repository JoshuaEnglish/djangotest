from django.contrib import admin

from .models import Role, Person, Team

admin.site.register(Role)
admin.site.register(Person)
admin.site.register(Team)
