# Generated by Django 5.0.4 on 2024-04-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myprofile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="blog_images/"),
        ),
    ]
