from django.shortcuts import render

# Create your views here.
def movies(request):
    return render(request, 'movies/movies.html')

def community(request):
    return render(request, 'movies/community.html')