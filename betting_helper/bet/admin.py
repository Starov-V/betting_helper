from django.contrib import admin

from .models import Bet, Team

admin.site.register(Bet)
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'league', 'id_on_api']
