from django.contrib import messages
from .forms import RecipeSearchForm
from .services import SpoonacularAPI
from django.core.paginator import Paginator
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


def search_recipes(request):
    results = []
    form = RecipeSearchForm()

    if 'query' in request.GET:
        form = RecipeSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            cuisine = form.cleaned_data['cuisine']
            diet = form.cleaned_data['diet']

            page = request.GET.get('page', 1)
            offset = (int(page) - 1) * 10

            api_response = SpoonacularAPI.search_recipes(
                query=query,
                cuisine=cuisine,
                diet=diet,
                number=10,
                offset=offset
            )

            if api_response and 'results' in api_response:
                results = api_response['results']
                total_results = api_response.get('totalResults', 0)

                paginator = Paginator(range(total_results), 10)
                page_obj = paginator.get_page(page)

    return render(request, 'recipes/search_results.html', {
        'form': form,
        'results': results,
        'page_obj': page_obj if 'page_obj' in locals() else None
    })


def recipe_detail_api(request, recipe_id):
    recipe = SpoonacularAPI.get_recipe_by_id(recipe_id)

    if not recipe:
        messages.error(request, "Recipe not found or API error occurred.")
        return redirect('recipe-list')

    return render(request, 'recipes/recipe_detail_api.html', {'recipe': recipe})