from django.urls import path
from . import views

app_name = 'trends'

urlpatterns = [
    path('keyword/', views.keyword, name='keyword'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('crawling/', views.crawling, name='crawling'),
    path('crawling_histogram/', views.crawling_histogram, name='crawling_histogram'),
    path('crawling_advanced/', views.crawling_advanced, name='crawling_advanced'),
]
