# Generated by Django 3.2.16 on 2022-12-03 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='author',
            new_name='recipe_name',
        ),
    ]
