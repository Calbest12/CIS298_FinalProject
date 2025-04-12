from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe-list'),
    path('add/', views.recipe_create, name='recipe-add'),
]