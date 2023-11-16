from config import celery_app
from fullcycledev.socials.helpers import (
    _get_discord_member_count,
    _get_twitch_follower_count,
    _get_youtube_subscriber_count,
)
from fullcycledev.socials.models import SocialStats


@celery_app.task()
def get_socials_stats():
    discord: int = _get_discord_member_count()
    twitch: int = _get_twitch_follower_count()
    youtube: int = _get_youtube_subscriber_count()

    SocialStats.objects.create(
        discord_members=discord,
        twitch_followers=twitch,
        youtube_subscribers=youtube,
    )
