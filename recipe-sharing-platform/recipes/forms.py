from django import forms
from .models import Recipe, Rating

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'category','image']


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
    ])
    diet = forms.ChoiceField(required=False, choices=[
        ('', 'No Dietary Restrictions'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('gluten free', 'Gluten Free'),
    ])

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']  # Rating field

    def __init__(self, *args, **kwargs):
        self.recipe = kwargs.pop('recipe', None)  # Pass recipe instance to the form
        super(RatingForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.recipe = self.recipe  # Link rating to the correct recipe
        self.instance.user = kwargs.pop('user')  # Link rating to the current user
        return super().save(*args, **kwargs)

