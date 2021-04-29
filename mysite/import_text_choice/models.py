from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField("Name", max_length=32)


class Territory(models.Model):
    name = models.CharField("Name", max_length=64)
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, related_name="territories"
    )

    def __str__(self):
        return f"{self.name}|{self.status}"

    def __repr__(self):
        return f"<Territory {self.name}>"
