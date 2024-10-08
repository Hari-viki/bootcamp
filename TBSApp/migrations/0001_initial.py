# Generated by Django 4.1.13 on 2024-09-24 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Routes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("train_number", models.CharField(max_length=255)),
                ("source_address", models.CharField(max_length=255)),
                ("desination_address", models.CharField(max_length=255)),
                ("stop1", models.CharField(max_length=255)),
                ("stop2", models.CharField(max_length=255)),
                ("stop3", models.CharField(max_length=255)),
                ("stop4", models.CharField(max_length=255)),
                ("stop5", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="UserRegister",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("phonenumber", models.BigIntegerField()),
                ("image", models.ImageField(upload_to="image")),
            ],
        ),
        migrations.CreateModel(
            name="payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.IntegerField()),
                (
                    "payment_method",
                    models.CharField(default="Processing", max_length=255),
                ),
                (
                    "train_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="TBSApp.routes"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="TBSApp.userregister",
                    ),
                ),
            ],
        ),
    ]
