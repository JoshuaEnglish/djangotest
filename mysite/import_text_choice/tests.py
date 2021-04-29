from django.test import TestCase

# Create your tests here.
from import_text_choice.models import Territory, Status
from import_text_choice.resources import TerritoryResource

from tablib import Dataset


class ImportTestCase(TestCase):
    def setUp(self):
        Status.objects.create(name="New")
        Status.objects.create(name="Continued")
        Status.objects.create(name="Removed")

    def test_basic_import(self):
        """importing with the choice's verbose name should encode correctly"""
        data = ["1", "Joes", "Continued"]

        territories = TerritoryResource()
        dataset = Dataset(data, headers=["id", "name", "status"])
        territories.import_data(dataset, dry_run=False)
        res = Territory.objects.get(name="Joes")
        self.assertEqual(res.status.name, "Continued")
        self.assertEqual(res.status_id, 2)
