from django.db import models

from fullcycledev.utils.models import BaseModel, SingletonModel


class SocialConfig(SingletonModel):
    substack_email = models.EmailField()
    substack_password = models.CharField(max_length=255)
    substack_publication_url = models.URLField()


class SocialStats(BaseModel):
    twitch_followers = models.IntegerField(default=0)
    youtube_subscribers = models.IntegerField(default=0)
    twitter_followers = models.IntegerField(default=0)
    substack_subscribers = models.IntegerField(default=0)
    discord_members = models.IntegerField(default=0)
