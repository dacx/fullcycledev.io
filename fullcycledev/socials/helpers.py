import requests
from substack import Api

from fullcycledev.socials.models import SocialConfig


def _get_discord_member_count():
    response = requests.get("https://discord.com/api/v9/invites/fUxexgvD4C?with_counts=true&with_expiration=true")
    return response.json()["approximate_member_count"]


def _get_substack_subscriber_count():
    config: SocialConfig = SocialConfig.load()
    api = Api(
        email=config.substack_email,
        password=config.substack_password,
        publication_url=config.substack_publication_url,
    )
    return api.get_publication_subscriber_count()
