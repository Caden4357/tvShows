from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def directors(request):
    context = {
        'directors': Director.objects.all()
    }
    return render(request, 'directors.html', context)
    

def create_director(request):
    if request.method == "POST":
        director = Director.objects.create(
            name=request.POST['name']
        )
    return redirect('/directors')
    


def destroy_director(request,id):
    return HttpResponse(f"Delete director{id}")

def show_director(request,id):
    return HttpResponse(f"Show one director {id}")
    
def movies(request):
        context = {
        'directors': Director.objects.all(),
        'movies': Movie.objects.all()
    }
        return render(request, 'movies.html', context)

def create_movie(request):
    if request.method == "POST":
        #validation
        errors = Movie.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request, value)
        return redirect('/movies')
        director = Director.objects.get(id=request.POST['director'])
        movie = Movie.objects.create(
        title=request.POST['title'],
        description = request.POST['description'],
        director = director
    )
    return redirect('/movies')
    
def show_movie(request,id):
    return HttpResponse(f"Placeholder for show one movie {id}details")

def edit_movie(request,id):
    if request.method == "POST":
        context = {
            'movie': Movie.objects.get(id=id),
            'directors': Director.objects.all()
        }
        return render(request, 'edit_movie.html', context)
    else:
        return redirect('/movies')


def update_movie(request,id):
    if request.method == "POST":
        movie_to_update = Movie.objects.get(id=id)
        movie_to_update.title = request.POST['title']
        movie_to_update.description = request.POST['description']
        movie_to_update.director = request.POST['director.id']
        movie_to_update.save()
    return redirect('/movies')

def destroy_movie(request,id):
    if request.method == "POST":
        movie_to_delete = Movie.objects.get(id=id)
        movie_to_delete.delete()
    return redirect('/movies')



