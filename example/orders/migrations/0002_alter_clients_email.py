# Generated by Django 3.2.5 on 2021-10-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]