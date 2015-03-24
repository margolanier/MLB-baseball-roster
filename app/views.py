#FILE: roster/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.shortcuts import render
from app.models import Team, Player


def home(request):
	team = Team.objects.all()
	return render(request, "app/home.html", {'team':team})

def team(request, pk):
	team = get_object_or_404(Team, id=pk)
	players = team.players.all()
	return render(request, "baseball/team.html", {
		'team': team, 
		'player':player
	})

def player(request, pk):
	player = get_object_or_404(Player, id=pk)
	return render(request, "basketball/player.html", {'player':player})


