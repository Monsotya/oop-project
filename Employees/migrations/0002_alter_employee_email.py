# Generated by Django 3.2.9 on 2021-11-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
