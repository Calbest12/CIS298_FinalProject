from django.urls import path
from .views import CustomLoginView, register_user, my_recipes, homepage
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib import messages

class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out.")
        return super().post(request, *args, **kwargs)

urlpatterns = [
    path('', homepage, name='home'),
    path('logout/', CustomLogoutView.as_view(next_page='home'), name='logout'),
    path('', views.recipe_list, name='recipe-list'),
    path('add/', views.recipe_create, name='recipe-add'),
    path('search/', views.search_recipes, name='recipe-search'),
    path('api/recipe/<int:recipe_id>/', views.recipe_detail_api, name='recipe-detail-api'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_user, name='register'),
    path('my-recipes/', my_recipes, name='recipe-my-list'),
    path('recipe/<int:pk>/', views.recipe_detail_local, name='recipe-detail-local'),
]