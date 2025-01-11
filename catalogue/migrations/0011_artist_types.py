# Generated by Django 4.2 on 2025-01-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='types',
            field=models.ManyToManyField(db_table='artist_type', related_name='artists', to='catalogue.type'),
        ),
    ]