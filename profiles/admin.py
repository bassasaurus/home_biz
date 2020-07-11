from django.contrib import admin
from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', ]


admin.site.register(Profile, ProfileAdmin)
