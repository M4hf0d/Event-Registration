# Generated by Django 4.1.2 on 2022-10-25 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_event_submission"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
