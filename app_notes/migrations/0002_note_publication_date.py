# Generated by Django 2.2 on 2021-08-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
