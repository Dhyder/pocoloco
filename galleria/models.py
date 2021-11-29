from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.



# Create your models here.
class Editor(models.Model):
    editor_name = models.CharField(max_length=30)
    email = models.EmailField()


    def __str__(self):
        return self.editor_name
    class Meta:
        ordering = ('editor_name',)

    def save_editor(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    location_name = models.CharField(max_length= 30)

    def __str__(self):
        return self.location_name

class Image(models.Model):
    img = CloudinaryField('chronicles/')
    img_name = models.CharField(max_length= 30)
    img_description = models.TextField()
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    editor = models.ForeignKey(Editor,on_delete = models.CASCADE)
    location = models.ForeignKey(Location,on_delete = models.CASCADE)

    def __str__(self):
        return self.img_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search):
        images = Image.objects.filter(category__name__icontains=search)
        return images