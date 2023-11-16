# Generated by Django 4.2.7 on 2023-11-16 12:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SocialConfig",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("twitch_client_secret", models.CharField(default="", max_length=255)),
                ("twitch_client_id", models.CharField(default="", max_length=255)),
                ("youtube_api_key", models.CharField(default="", max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SocialStats",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("twitch_followers", models.IntegerField(default=0)),
                ("youtube_subscribers", models.IntegerField(default=0)),
                ("twitter_followers", models.IntegerField(default=0)),
                ("discord_members", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ("-created", "-modified"),
                "abstract": False,
            },
        ),
    ]
