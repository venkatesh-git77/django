from django.shortcuts import render
from .form import MovieForm

# Create your views here.

def index(request):
    return render(request,'newMoviewRating/index.html')


def addMoviewRating(request):
    form = MovieForm(request.POST)
    if request.method == "POST":
        if form.is_valid:
            form.save()

    return render(request,'newMoviewRating/addrating.html',{'form':form})
