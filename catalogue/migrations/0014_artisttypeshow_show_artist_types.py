# Generated by Django 5.1.2 on 2025-01-11 03:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_artisttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistTypeShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artistTypeShows', to='catalogue.artisttype')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artistTypeShows', to='catalogue.show')),
            ],
            options={
                'db_table': 'artist_type_show',
                'unique_together': {('show', 'artist_type')},
            },
        ),
        migrations.AddField(
            model_name='show',
            name='artist_types',
            field=models.ManyToManyField(related_name='shows', through='catalogue.ArtistTypeShow', to='catalogue.artisttype'),
        ),
    ]
