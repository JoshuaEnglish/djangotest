from import_export import resources

from .models import Territory


class TerritoryResource(resources.ModelResource):
    class Meta:
        model = Territory
        skip_unchanged = True
        fields = ("id", "name", "status")
