from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.TextChoices):
    NEW = "NEW", _("New")
    CONTINUED = "CNT", _("Continued")
    REMOVED = "RMV", _("Removed")


class Territory(models.Model):
    name = models.CharField("Name", max_length=64)
    status = models.CharField(
        "Status", max_length=3, choices=Status.choices, default=Status.NEW
    )

    def __str__(self):
        return f"{self.name}|{self.status}"

    def __repr__(self):
        return f"<Territory {self.name}>"
