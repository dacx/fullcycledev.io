import requests

from fullcycledev.socials.models import SocialConfig


def _get_discord_member_count():
    response = requests.get("https://discord.com/api/v9/invites/fUxexgvD4C?with_counts=true&with_expiration=true")
    return response.json()["approximate_member_count"]


def _get_youtube_subscriber_count():
    config: SocialConfig = SocialConfig.load()
    channel: str = "UC3XQw149GcyW0nIQ0S3_UGw"
    return requests.get(
        f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel}&key={config.youtube_api_key}"
    ).json()["items"][0]["statistics"]["subscriberCount"]


def _get_twitch_follower_count():
    # create a content type url-encoded header and then pass the auth creds
    config: SocialConfig = SocialConfig.load()

    response = requests.post(
        "https://id.twitch.tv/oauth2/token",
        data={
            "client_id": config.twitch_client_id,
            "client_secret": config.twitch_client_secret,
            "grant_type": "client_credentials",
        },
    )

    access_token = response.json()["access_token"]

    response = requests.get(
        "https://api.twitch.tv/helix/channels/followers",
        headers={
            "Authorization": f"Bearer {access_token}",
            "client-id": config.twitch_client_id,
        },
        params={
            "broadcaster_id": "38308407",
        },
    )

    return response.json()["total"]
