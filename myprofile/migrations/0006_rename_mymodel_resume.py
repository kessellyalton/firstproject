# Generated by Django 5.0.6 on 2024-06-19 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myprofile", "0005_alter_mymodel_options_mymodel_description_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MyModel",
            new_name="Resume",
        ),
    ]
