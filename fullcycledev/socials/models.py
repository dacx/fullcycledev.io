from django.db import models

from fullcycledev.utils.models import BaseModel, SingletonModel


class SocialConfig(SingletonModel):
    twitch_client_secret = models.CharField(max_length=255, default="")
    twitch_client_id = models.CharField(max_length=255, default="")
    youtube_api_key = models.CharField(max_length=255, default="")


class SocialStats(BaseModel):
    twitch_followers = models.IntegerField(default=0)
    youtube_subscribers = models.IntegerField(default=0)
    twitter_followers = models.IntegerField(default=0)
    discord_members = models.IntegerField(default=0)
