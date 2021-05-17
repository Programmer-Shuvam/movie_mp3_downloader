from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home.html")

def home(request):
    return render(request,"home.html")

def bollywood(request):
    return render(request,"bollywood.html")

def hollywood(request):
    return render(request,"hollywood.html")

def pcgames(request):
    return render(request,"pcgames.html")

def music(request):
    return render(request,"music.html")

def search(request):

    val = request.GET["search"]
    print(val)
    # return render(request,"home.html")