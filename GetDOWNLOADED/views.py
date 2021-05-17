from django.shortcuts import render
from django.http import *
from . import models
from django.contrib import messages
from django.db.models import Q


def index(request):
    icons = models.bollywood.objects.all()
    return render(request, "home.html", {'icons': icons, })


def bollywood(request):
    icons = models.bollywood.objects.all()
    return render(request, "bollywood.html", {'icons': icons})


def hollywood(request):
    icons = models.hollywood.objects.all()
    return render(request, "hollywood.html", {'icons': icons})


def pcgames(request):
    icons = models.pcgames.objects.all()
    return render(request, "pcgames.html", {'icons': icons})


def music(request):
    icons = models.music.objects.all()
    return render(request, "music.html", {'icons': icons})


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            bolly = models.bollywood.objects.filter(Q(name__unaccent__lower__trigram_similar=srch) | Q(
                desc__unaccent__lower__trigram_similar=srch))
            holly = models.hollywood.objects.filter(Q(name__unaccent__lower__trigram_similar=srch) | Q(
                desc__unaccent__lower__trigram_similar=srch))
            games = models.pcgames.objects.filter(Q(name__unaccent__lower__trigram_similar=srch) | Q(
                desc__unaccent__lower__trigram_similar=srch))
            songs = models.music.objects.filter(Q(name__unaccent__lower__trigram_similar=srch) | Q(
                desc__unaccent__lower__trigram_similar=srch))
            sr = []
            if bolly:
                sr.append(bolly)
            if holly:
                sr.append(holly)
            if games:
                sr.append(games)
            if songs:
                sr.append(songs)
            if len(sr) != 0:
                return render(request, "search.html", {'sr': sr})
            else:
                return render(request, "countdown.html", {'value': srch})
        else:
            return HttpResponseRedirect('/search/')
    return render(request, "search.html")
