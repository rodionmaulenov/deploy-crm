# Generated by Django 4.2 on 2023-05-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=250, null=True),
        ),
    ]