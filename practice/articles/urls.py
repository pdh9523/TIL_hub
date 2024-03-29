from django.urls import path
from . import views

# 무슨 앱을 위한 urls인지 namespace 설정해두기
app_name = "articles"
urlpatterns = [
    path('',views.index, name="index"),
    path('create/', views.create, name="create"),
]
