# Generated by Django 4.2.7 on 2023-11-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("socials", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialConfig",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("substack_email", models.EmailField(max_length=254)),
                ("substack_password", models.CharField(max_length=255)),
                ("substack_publication_url", models.URLField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]