from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe-list'),
    path('add/', views.recipe_create, name='recipe-add'),
    path('search/', views.search_recipes, name='recipe-search'),
    path('api/recipe/<int:recipe_id>/', views.recipe_detail_api, name='recipe-detail-api'),
]