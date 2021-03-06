# Generated by Django 2.1.2 on 2018-10-09 15:51

from django.db import migrations
import random


def create_random_relations(apps, schema_editor):
    Developer = apps.get_model("searchapp", 'Developer')
    ProgrammingLanguage = apps.get_model("searchapp", 'ProgrammingLanguage')
    Language = apps.get_model("searchapp", 'Language')

    for i in range(1, 101):
        dev = Developer.objects.get(pk=i)

        dev.programming_languages.clear()
        dev.languages.clear()

        for _ in range(0, random.randint(1, 7)):
            dev.programming_languages.add(ProgrammingLanguage.objects.get(pk=random.randint(1, 7)))

        for _ in range(0, random.randint(1, 4)):
            dev.languages.add(Language.objects.get(pk=random.randint(1, 4)))


class Migration(migrations.Migration):
    dependencies = [
        ('searchapp', '0002_auto_20181005_1758'),
    ]

    operations = [
        migrations.RunPython(create_random_relations),
    ]
