# Generated by Django 3.1.7 on 2021-04-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]