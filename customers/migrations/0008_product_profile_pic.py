# Generated by Django 4.2 on 2023-05-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
