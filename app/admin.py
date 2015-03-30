from django.contrib import admin
from app.models import League, Team, Player

class LeagueAdmin(admin.ModelAdmin):
	search_fields = ('name',)

class TeamAdmin(admin.ModelAdmin):
	search_fields = ('name',)

class PlayerAdmin(admin.ModelAdmin):
	search_fields = ('name',)

# Register your models here.
admin.site.register(League, LeagueAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)