# Generated by Django 4.0.4 on 2022-07-13 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
