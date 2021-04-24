"""Models

The problem I'm trying to recreate and solve is in the models below, the
admin screen, when adding a team, does not limit the choices appropriately.
"""

from django.db import models

# Create your models here.
class Role(models.Model):
    """
    Role is a separate model because the full app caries extra 
    information that is not relevant to this problem.
    """
    name = models.CharField("Name", max_length=32)

    def __str__(self):
        return self.name

class Person(models.Model):
    """
    Person - name and role as ForeignKey
    """
    name = models.CharField("Name", max_length=64)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} ({self.role.name})"

class Team(models.Model):
    """
    Team - one sales team can have multiple sales reps and multiple
    engineers, and a Person can be on multiple teams
    """
    rep = models.ManyToManyField(
        Person,
        related_name = "rep_on",
        verbose_name="Sales Rep",
        limit_choices_to={'role__name': 'Sales Rep'})
    eng = models.ManyToManyField(
        Person,
        related_name = "eng_on",
        verbose_name="Engineer",
        limit_choices_to={'role__name': 'Engineer'})

    def __str__(self):
        return ",".join([p.name for p in self.rep.all()])

