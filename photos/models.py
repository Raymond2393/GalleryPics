from django.db import models

# Create your models here.
class Location(models.Model):
    place = model.CharField(max_length=30)

    def __str__(self):
        return self.place
        class Meta:
            ordering = ['place']

    def save_location(self):
        self.save()
class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()
