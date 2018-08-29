# Generated by Django 2.1 on 2018-08-28 17:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandate', '0003_add_twitter_id_as_big_integer'),
    ]

    operations = [
        migrations.CreateModel(
            name='LawProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('url_id', models.IntegerField()),
                ('area', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), size=None)),
                ('original_keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), size=None)),
                ('url', models.URLField(max_length=250)),
                ('authors', models.ManyToManyField(to='mandate.Politician')),
            ],
        ),
    ]