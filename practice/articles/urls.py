from django.urls import path
from . import views

# 무슨 앱을 위한 urls인지 namespace 설정해두기
app_name = "articles"
urlpatterns = [
    path('',views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:article_pk>/comments/', views.create_comments, name='create_comments'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comments, name="delete_comments"),
]
