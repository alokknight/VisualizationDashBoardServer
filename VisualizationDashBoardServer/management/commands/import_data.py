from django.core.management.base import BaseCommand
from dashapi.models import DataPoint
import json

class Command(BaseCommand):
    help = 'Import data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file to import')

    def handle(self, *args, **options):
        json_file_path = options['json_file']

        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)


        for item in data:
            DataPoint.objects.create(
            end_year=   item['end_year'],
            intensity=  item['intensity'],
            sector=     item['sector'],
            topic=      item['topic'],
            insight=    item['insight'],
            url=        item['url'],
            region=     item['region'],
            start_year= item['start_year'],
            impact=     item['impact'],
            added=      item['added'],
            published=  item['published'],
            country=    item['country'],
            relevance=  item['relevance'],
            pestle=     item['pestle'],
            source=     item['source'],
            title=      item['title'],
            likelihood= item['likelihood'],
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
