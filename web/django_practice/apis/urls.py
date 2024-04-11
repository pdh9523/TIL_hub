from django.urls import path
from . import views

urlpatterns = [
    path('apis/', views.api_list),
    path('apis/<int:api_pk>/', views.api_detail),
]
