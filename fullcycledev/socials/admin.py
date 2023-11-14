from django.contrib import admin

from fullcycledev.socials.models import SocialStats, SocialConfig

# Register your models here.
admin.site.register(SocialStats)
admin.site.register(SocialConfig)
