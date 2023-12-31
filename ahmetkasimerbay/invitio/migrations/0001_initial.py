# Generated by Django 4.2.4 on 2023-08-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Guest",
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
                ("g_id", models.IntegerField()),
                ("g_name", models.CharField(max_length=30)),
                ("g_surname", models.CharField(max_length=20)),
                ("g_adult", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Persons",
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
                ("p_name", models.CharField(max_length=30)),
                ("p_surname", models.CharField(max_length=20)),
                ("p_is_alone", models.BooleanField()),
                ("p_adult", models.BooleanField()),
                ("p_num_guests", models.IntegerField()),
                (
                    "p_attandance_status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Katılılyorum"),
                            (2, "Katılamıyorum"),
                            (3, "Belli Değil"),
                        ],
                        default=0,
                    ),
                ),
                ("p_phone", models.CharField(max_length=13)),
                ("p_message", models.TextField()),
                ("p_register_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
