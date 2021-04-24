from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField("Name", max_length=32)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField("Name", max_length=64)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} ({self.role.name})"

class Team(models.Model):
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

