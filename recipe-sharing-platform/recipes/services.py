import requests
from django.conf import settings


class SpoonacularAPI:
    BASE_URL = "https://api.spoonacular.com"

    @staticmethod
    def search_recipes(query, cuisine=None, diet=None, number=10, offset=0):
        endpoint = f"{SpoonacularAPI.BASE_URL}/recipes/complexSearch"

        params = {
            'apiKey': settings.SPOONACULAR_API_KEY,
            'query': query,
            'number': number,
            'offset': offset,
            'addRecipeInformation': True,
            'fillIngredients': True,
        }

        if cuisine:
            params['cuisine'] = cuisine
        if diet:
            params['diet'] = diet

        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def get_recipe_by_id(recipe_id):
        endpoint = f"{SpoonacularAPI.BASE_URL}/recipes/{recipe_id}/information"

        params = {
            'apiKey': settings.SPOONACULAR_API_KEY,
            'includeNutrition': False,
        }

        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            return response.json()
        return None