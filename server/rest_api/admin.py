from django.contrib import admin
from rest_api.models import App, Platform, Repo, Article


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon')

admin.site.register(App)
admin.site.register(Repo)
admin.site.register(Article)
admin.site.register(Platform, PlatformAdmin)
