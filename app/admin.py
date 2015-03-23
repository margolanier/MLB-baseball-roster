from django.contrib import admin
from app.models import Team, Player

class TeamAdmin(admin.ModelAdmin):
	search_fields = ('name',)

class PlayerAdmin(admin.ModelAdmin):
	search_fields = ('name',)

# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)