from django.shortcuts import render
from uuid import uuid4
from django.http import *
from . import models
from django.contrib import messages
from django.db.models import Q
from scrapyd_api import ScrapydAPI
import ast


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
    return render(request, "music454.html", {'icons': icons})


scrapyd = ScrapydAPI('http://localhost:6800')


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
            if sr == []:
                # unique_id = str(uuid4())
                task = scrapyd.schedule('default', 'yts_django', url=srch)
                return render(request, "countdown.html", {'val': srch})

            else:
                return render(request, "search.html", {'sr': sr})
        # else:
        # messages.error(request,'NO SUCH RESULT FOUND !!!')
        else:
            return HttpResponseRedirect('/search/')
    return render(request, "search.html")


##########################
##  variable niche hai  ##
##########################
# fetched_data = {
#     'The Avengers__1':
#         {'1080p.BluRay': ' 699.73 MB <>https://yts.mx/torrent/download/26036FC18C34D74AD31E3879AF3A575F0C8A511B',
#          'Download Subtitles': ' 1.24 GB <>https://yifysubtitles.org/movie-imdb/tt0118661',
#          'cover': 'https://img.yts.mx/assets/images/movies/The_Avengers_1998/medium-cover.jpg',
#          'screenshot': ['https://img.yts.mx/assets/images/movies/The_Avengers_1998/large-screenshot1.jpg', 'https://img.yts.mx/assets/images/movies/The_Avengers_1998/large-screenshot2.jpg', 'https://img.yts.mx/assets/images/movies/The_Avengers_1998/large-screenshot3.jpg'],
#          'descrip': ' British Ministry Agent John Steed, under direction from "Mother", investigates a diabolical plot by archvillain Sir August de Wynter to rule the world with his weather control machine. Steed investigates the beautiful Doctor Mrs. Emma Peel, the only suspect, but simultaneously falls for her and joins forces with her to combat Sir August. ',
#          'duration': ' 1 hr 29 min ',
#          'rel_date': [2020, 4, 7]},

#     'Avengers: Endgame':
#         {'720p.BluRay': ' 2.84 GB <>https://yts.mx/torrent/download/5A4140BD59D66BCAC57CF05AF4A8FAB4EBCAE1C1',
#          '1080p.BluRay': ' 1.43 GB <>https://yts.mx/torrent/download/223F7484D326AD8EFD3CF1E548DED524833CB77E',
#          '2160p.BluRay': ' 3.01 GB <>https://yts.mx/torrent/download/709FBD48374D2AE13C11B07A26B5E7DDC727D720',
#          '720p.WEB': ' 5.26 GB <>https://yts.mx/torrent/download/9D62160EEE330397A7A7BABA989A269C58CCFD8E',
#          '1080p.WEB': ' 1.43 GB <>https://yts.mx/torrent/download/414A6F933C48FC7543A9CDB42C854B5457C5BCC7',
#          'Download Subtitles': ' 3 GB <>https://yifysubtitles.org/movie-imdb/tt4154796',
#          'cover': 'https://img.yts.mx/assets/images/movies/avengers_endgame_2019/medium-cover.jpg',
#          'screenshot': ['https://img.yts.mx/assets/images/movies/avengers_endgame_2019/large-screenshot1.jpg', 'https://img.yts.mx/assets/images/movies/avengers_endgame_2019/large-screenshot2.jpg', 'https://img.yts.mx/assets/images/movies/avengers_endgame_2019/large-screenshot3.jpg'],
#          'descrip': " After the devastating events of Avengers: Infinity War (2018), the universe is in ruins due to the efforts of the Mad Titan, Thanos. With the help of remaining allies, the Avengers must assemble once more in order to undo Thanos's actions and undo the chaos to the universe, no matter what consequences may be in store, and no matter who they face... ",
#          'duration': ' 3 hr 1 min ',
#          'rel_date': [2020, 4, 7]},

#     'Avengers: Infinity War':
#         {'720p.BluRay': ' 2.39 GB <>https://yts.mx/torrent/download/EA17E6BE92962A403AC1C638D2537DCF1E564D26',
#          '1080p.BluRay': ' 1.25 GB <>https://yts.mx/torrent/download/866BDCFA006930A718ADBC21D8CAE1F2C7F9D8B3',
#          '2160p.BluRay': ' 2.39 GB <>https://yts.mx/torrent/download/F99044B231A20F0825E4163B31AF3BA7A7AD3464',
#          '720p.WEB': ' 7.32 GB <>https://yts.mx/torrent/download/BCEB706EA32EDD855FCA4426DF8A7831F53CC3EE',
#          '1080p.WEB': ' 1.24 GB <>https://yts.mx/torrent/download/7643D0625DED0A5FC967B37A9D6AF6990236C180',
#          'Download Subtitles': ' 2.39 GB <>https://yifysubtitles.org/movie-imdb/tt4154756',
#          'cover': 'https://img.yts.mx/assets/images/movies/avengers_infinity_war_2018/medium-cover.jpg',
#          'screenshot': ['https://img.yts.mx/assets/images/movies/avengers_infinity_war_2018/large-screenshot1.jpg', 'https://img.yts.mx/assets/images/movies/avengers_infinity_war_2018/large-screenshot2.jpg', 'https://img.yts.mx/assets/images/movies/avengers_infinity_war_2018/large-screenshot3.jpg'],
#          'descrip': ' As the Avengers and their allies have continued to protect the world from threats too large for any one hero to handle, a new danger has emerged from the cosmic shadows: Thanos. A despot of intergalactic infamy, his goal is to collect all six Infinity Stones, artifacts of unimaginable power, and use them to inflict his twisted will on all of reality. Everything the Avengers have fought for has led up to this moment, the fate of Earth and existence has never been more uncertain. ',
#          'duration': ' 2 hr 29 min ',
#          'rel_date': [2020, 4, 7]},
# }
