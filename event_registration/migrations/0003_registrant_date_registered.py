# Generated by Django 3.1.2 on 2020-10-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration', '0002_auto_20201018_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrant',
            name='date_registered',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
