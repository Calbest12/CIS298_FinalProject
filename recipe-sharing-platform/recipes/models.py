from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    def update_rating(self):
        # Update the rating with the average score from all ratings
        ratings = Rating.objects.filter(recipe=self)
        if ratings.exists():
            self.rating = ratings.aggregate(Avg('score'))['score__avg']
        else:
            self.rating = 0.0
        self.save()

    def __str__(self):
        return self.title

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5

    def __str__(self):
        return f'{self.user.username} rated {self.recipe.title} - {self.score}'

class Comment(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.recipe.title}"

