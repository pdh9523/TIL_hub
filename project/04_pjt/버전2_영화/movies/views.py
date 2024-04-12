from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()

    context = {
        'movies' : movies,
    }

    return render(request, 'movies/index.html', context)

def create(request):
    # 글을 쓰는 경우
    if request.method == "POST" :
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)

    # 글을 쓰려 들어가는 경우
    form = MovieForm()

    context = {
        'form' : form,
    }
    return render(request, 'movies/create.html', context)

def update(request, movie_pk):
    # 수정을 하고 싶다
    # 1. 뭘 수정할거냐?
    # 2. 어떻게 수정할거냐?
    # 3. 수정한거? 제출은 어떻게 할거냐?

    movie = Movie.objects.get(pk=movie_pk)
    # 1) 수정한 글을 저장하는 경우
    if request.method == "POST" :
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)

    # 2) 수정하려고 들어가는 경우
    form = MovieForm(instance=movie)
    
    context = {
        'form' : form,
    }
    return render(request, 'movies/update.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    
    movie.delete()
    return redirect('movies:index')