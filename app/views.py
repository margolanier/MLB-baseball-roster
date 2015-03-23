from django.db import HttpResponse

def home(request):
    return HttpResponse('Hello World!')

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from baseball.models import Team, Player


def home(request):
	team = Team.objects.all()
	return render(request, "baseball/home.html", {'team':team})

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


