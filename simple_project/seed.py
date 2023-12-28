import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_project.settings')
django.setup()

from simple_app.models import Item

ITEMS=100



def fake_data(num_entries=ITEMS):
    fake = Faker()

    for _ in range(num_entries):
        name = fake.word()
        description = fake.text()

        item = Item.objects.create(name=name, description=description)
        item.save()

    print(f"{num_entries} entries added to the database.")

if __name__ == '__main__':
    fake_data()