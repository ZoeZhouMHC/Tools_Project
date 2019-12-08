from django.core.management.base import BaseCommand
from sightings.models import Sighting
import csv
import datetime

class Command(BaseCommand):
    def add_arguments(self, parser): 
        parser.add_argument('csv_file') 
    def handle(self, *args, **options): 
        def func(x):
            if x.lower() == 'true':
                return 'True'
            else:
                return 'False'

        with open(options['csv_file']) as fp: 
            reader = csv.DictReader(fp) 
            data = list(reader) 
            for row in data: 
                s = Sighting(latitude = float(row['Y']),
                longitude = float(row['X']),
                unique_squirrel_id = row['Unique Squirrel ID'],
                shift = row['Shift'],
                date = datetime.datetime.strptime(row['Date'],'%m%d%Y'),
                age = row['Age'].capitalize(),
                primary_fur_color = row['Primary Fur Color'].capitalize(),
                location = row['Location'].capitalize(),
                specific_location = row['Specific Location'].capitalize(),
                running = func(row['Running'].capitalize()),
                chasing = func(row['Chasing'].capitalize()),
                climbing = func(row['Climbing'].capitalize()),
                eating = func(row['Eating'].capitalize()),
                foraging = func(row['Foraging'].capitalize()),
                other_activities = row['Other Activities'].capitalize(),
                kuks = func(row['Kuks'].capitalize()),
                quaas = func(row['Quaas'].capitalize()),
                moans = func(row['Moans'].capitalize()),
                tail_flags =func(row['Tail flags'].capitalize()),
                tail_twitches = func(row['Tail twitches'].capitalize()),
                approaches = func(row['Approaches'].capitalize()),
                indifferent = func(row['Indifferent'].capitalize()),
                runs_from = func(row['Runs from'].capitalize()),
                )
                s.save()

