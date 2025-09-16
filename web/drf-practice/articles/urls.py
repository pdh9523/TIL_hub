from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list_create, name='article_list_create'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/comments/', views.comment_list_create, name='comment_list_create'),
    path('comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
]