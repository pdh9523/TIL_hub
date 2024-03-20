from django.urls import path
from . import views
app_name="movies"
urlpatterns = [
    path('', views.movies, name='main'),
    path('community/', views.community, name='community'),
]
