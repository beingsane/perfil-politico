# Generated by Django 2.1 on 2018-08-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandate', '0004_lawproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawproject',
            name='area',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lawproject',
            name='url',
            field=models.URLField(max_length=500),
        ),
    ]