from django.core.management.base import BaseCommand,CommandError
import csv
import datetime
from sightings.models import Sighting
from django.http import HttpResponse
import sys

class Command(BaseCommand):
    help = ("Output Squirrels'Sightings as csv")

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        field_names = [f.name for f in Sighting._meta.fields]

        with open(path, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(field_names)
            for instance in Sighting.objects.all():
                writer.writerow([getattr(instance, f) for f in field_names])

