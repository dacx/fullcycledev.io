# Generated by Django 4.2.7 on 2023-11-17 10:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("socials", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="socialstats",
            options={"ordering": ["-created"], "verbose_name_plural": "Social Stats"},
        ),
    ]
