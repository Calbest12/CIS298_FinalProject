from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required


def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe-list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})
