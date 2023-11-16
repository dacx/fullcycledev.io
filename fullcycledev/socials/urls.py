from django.urls import path

from fullcycledev.socials.views import twitch_oauth_callback_handler

app_name = "socials"
urlpatterns = [
    path("twitch/callback/", view=twitch_oauth_callback_handler, name="twitch_oauth_callback_handler"),
]
