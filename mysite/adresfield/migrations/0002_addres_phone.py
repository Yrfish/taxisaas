# Generated by Django 3.2 on 2023-02-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adresfield', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addres',
            name='phone',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Phone'),
            preserve_default=False,
        ),
    ]