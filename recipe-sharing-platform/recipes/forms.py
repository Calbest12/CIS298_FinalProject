from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'category']


class RecipeSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Search recipes...'}))
    cuisine = forms.ChoiceField(required=False, choices=[
        ('', 'Any Cuisine'),
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('indian', 'Indian'),
        ('chinese', 'Chinese'),
        ('american', 'American'),
        # Add more cuisines as needed
    ])
    diet = forms.ChoiceField(required=False, choices=[
        ('', 'No Dietary Restrictions'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('gluten free', 'Gluten Free'),
    ])