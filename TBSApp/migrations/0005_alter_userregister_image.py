# Generated by Django 4.1.13 on 2024-09-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TBSApp", "0004_alter_payment_payment_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userregister",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="image"),
        ),
    ]
