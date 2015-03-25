#FILE: roster/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.shortcuts import render
from app.models import Team, Player


def home(request):
	team = Team.objects.all()
	return render(request, "baseball/home.html", {
		'team':team,
		'player_count': Player.objects.count(),
		'team_count': Team.objects.count(),
	})

# list of all teams
def teamList(request):
    teams = Team.objects.all()
    return render(request, 'baseball/teams.html', {'teams': teams})

# single team page
def team(request, team_pk):
	team = get_object_or_404(Team, id=team_pk)
	players = team.players.all()
	return render(request, "baseball/team.html", {
		'team': team, 
		'player':player
	})

# list of all players
def playerList(request):
    players = Player.objects.all()
    return render(request, 'baseball/players.html', {'players': players})

# single player page
def player(request, player_pk):
	player = get_object_or_404(Player, id=player_pk)
	return render(request, "baseball/player.html", {'player':player})


