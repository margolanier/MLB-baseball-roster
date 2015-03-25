#FILE: roster/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.shortcuts import render
from app.models import Team, Player


def home(request):
	team = Team.objects.all()
	return render(request, "app/home.html", {'team':team})

def team(request, team_pk):
	team = get_object_or_404(Team, id=team_pk)
	players = team.players.all()
	return render(request, "baseball/team.html", {
		'team': team, 
		'player':player
	})

def player(request, player_pk):
	player = get_object_or_404(Player, id=player_pk)
	return render(request, "baseball/player.html", {'player':player})


