from django.db import models
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['description']) == 0:
            description = ['description']
        elif len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['d'] = 'description minimum number of characters is 10'
        if len(postData['title']) < 2:
            errors["title"] = "Show name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['release_date']) < 8:
            errors['release_date'] = "Show release date should be 8 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    release_date = models.DateField()
    network = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
