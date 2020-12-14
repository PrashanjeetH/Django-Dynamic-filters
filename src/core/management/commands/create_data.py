from django.core.management.base import BaseCommand
import random
import datetime
from core.models import Author, Category, Journal
Categories = [
    'Sports',
    'Lifestyle',
    'Music',
    'Coding',
    'Travelling',
]

Authors = [
    'John', 'Michael', 'Luke', 'Sally', 'Joe', 'Jeetu',
]


def generate_author_name():
    index = random.randint(0, 5)
    return Authors[index]


def generate_category_name():
    index = random.randint(0, 4)
    return Categories[index]


def generate_views_count():
    count = random.randint(0, 100)
    return count


def generate_is_reviewed():
    value = random.randint(0, 1)
    if value==0:
        return False
    return True


def generate_published_date():
    year = random.randint(2019, 2020)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help="The text file that contains the journal title")

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                title = row
                author_name = generate_author_name()
                category_name = generate_category_name()
                publish_date = generate_published_date()
                views_count = generate_views_count()
                reviewed = generate_is_reviewed()

                author = Author.objects.get_or_create(
                    name=author_name
                )

                journal = Journal(
                    title=title,
                    author=Author.objects.get(name=author_name),
                    publish_date=publish_date,
                    views=views_count,
                    reviewed=reviewed,
                )

                journal.save()

                category = Category.objects.get_or_create(name=category_name)

                journal.categories.add(Category.objects.get(name=category_name))

            self.stdout.write(self.style.SUCCESS('Data Imported Successfully'))
