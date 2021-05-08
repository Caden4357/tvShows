from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class MovieManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["name"] = "Movie name should be at least 2 characters"
        if len(postData['description']) < 5:
            errors["description"] = "Movie description should be at least 5 characters"

        return errors

class Movie(models.Model):
    title = models.CharField(max_length=250)
    description=models.CharField(max_length=255)
    director =models.ForeignKey(Director,related_name="movies", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = MovieManager()

class Actor(models.Model):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie, related_name='actors')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)