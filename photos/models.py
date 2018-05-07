from django.db import models

# Create your models here.
class Location(models.Model):
    place = models.CharField(max_length=30)

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

    @classmethod
    def my_images(Cls):
        images = cls.objects.all()
        return Images
    def save_images(self):
        self.remove()
    def delete_images(self):
        self.remove()
    def update_image(self, id):
        pass
    def get_image_by_id(id):
        pass
    def filter_by_location(location):
        pass
    def search_image(category):
        pass


    @classmethod
    def search_by_category(cls, search_term):
        category = cls.objects.filter(category__category__icontains=search_term)
        return category
