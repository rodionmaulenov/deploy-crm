# Generated by Django 4.2 on 2023-05-01 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_order_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_crated',
            new_name='date_created',
        ),
    ]
