from django.db.models import QuerySet
from django.http import HttpRequest
from django.shortcuts import render

from fullcycledev.socials.models import SocialStats
from fullcycledev.users.models import User


def home(request: HttpRequest):
    stats: QuerySet[SocialStats] = SocialStats.objects.all()[:2]
    current: SocialStats = stats[0]
    delta: dict = {
        "twitch_followers": current.twitch_followers - stats[1].twitch_followers,
        "youtube_subscribers": current.youtube_subscribers - stats[1].youtube_subscribers,
        "twitter_followers": current.twitter_followers - stats[1].twitter_followers,
        "discord_members": current.discord_members - stats[1].discord_members,
    }
    users_count: int = User.objects.count()

    return render(request, "pages/home.html", {"current": current, "delta": delta, "users_count": users_count})
