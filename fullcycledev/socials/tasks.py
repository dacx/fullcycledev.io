from config import celery_app
from fullcycledev.socials.helpers import _get_discord_member_count, _get_substack_subscriber_count
from fullcycledev.socials.models import SocialStats


@celery_app.task()
def get_socials_stats():
    discord: int = _get_discord_member_count()
    substack: int = _get_substack_subscriber_count()
    SocialStats.objects.create(
        discord_members=discord,
        substack_subscribers=substack,
    )
