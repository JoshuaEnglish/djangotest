from django.contrib import admin

from .models import Role, Person, Team


class RepInline(admin.TabularInline):
    model = Team.rep.through


class EngInline(admin.TabularInline):
    model = Team.eng.through


class TeamAdmin(admin.ModelAdmin):
    inlines = [RepInline, EngInline]


admin.site.register(Role)
admin.site.register(Person)
admin.site.register(Team, TeamAdmin)
