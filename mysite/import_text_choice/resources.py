from import_export import resources, fields, widgets

from .models import Territory, Status


class TerritoryResource(resources.ModelResource):
    status = fields.Field(
        attribute="status", widget=widgets.ForeignKeyWidget(Status, "name")
    )

    class Meta:
        model = Territory
        skip_unchanged = True
        fields = ("id", "name", "status")
