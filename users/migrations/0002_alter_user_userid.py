# Generated by Django 3.2.8 on 2021-10-14 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.IntegerField(null=True),
        ),
    ]
