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

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/',null=True, blank=True)
    image_name =models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    loaction = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name
