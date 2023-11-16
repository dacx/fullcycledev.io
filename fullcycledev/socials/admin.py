from django.contrib import admin

from fullcycledev.socials.models import SocialConfig, SocialStats

admin.site.register(SocialConfig)


@admin.register(SocialStats)
class SocialStatsAdmin(admin.ModelAdmin):
    list_display = [
        "twitch_followers",
        "youtube_subscribers",
        "twitter_followers",
        "discord_members",
        "created",
    ]
