from django.shortcuts import render
from .models import Player, Game


def show_home(request):
    # Check if there are existing games


    return render(
        request,
        'home.html'
    )
