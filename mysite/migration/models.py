from django.db import models


class Status(models.Model):
    name = models.CharField("Name", max_length=32)


class Thing(models.Model):
    name = models.CharField("Name", max_length=64)
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, related_name="things"
    )
