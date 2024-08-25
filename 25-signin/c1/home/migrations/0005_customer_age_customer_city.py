# Generated by Django 5.0 on 2024-07-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_customer_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=26),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='Tehran', max_length=200),
        ),
    ]
