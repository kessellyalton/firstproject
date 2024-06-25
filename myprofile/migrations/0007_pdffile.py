# Generated by Django 5.0.6 on 2024-06-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myprofile", "0006_rename_mymodel_resume"),
    ]

    operations = [
        migrations.CreateModel(
            name="PDFFile",
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
                ("title", models.CharField(max_length=255)),
                ("file", models.FileField(upload_to="pdfs/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]