import json
from csv import reader

from django.core.management.base import BaseCommand

from .models import Ingredient, Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("./data/ingredients.csv", "r", encoding="UTF-8") \
                as ingredients:
            for i in reader(ingredients):
                if len(i) == 2:
                    Ingredient.objects.get_or_create(
                        name=i[0],
                        measurement_unit=i[1],
                    )
        with open('data/tags.json', encoding='utf-8',
                  ) as data_file_tags:
            tags_data = json.loads(data_file_tags.read())
            for tags in tags_data:
                Tag.objects.get_or_create(**tags)
