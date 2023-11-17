from django.urls import path

from fullcycledev.socials.views import home

app_name = "socials"
urlpatterns = [
    path("", view=home, name="home"),
]
