# Generated by Django 3.1.3 on 2020-11-11 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]