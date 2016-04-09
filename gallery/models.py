from django.db import models

# Create your models here.
class Gallery(models.Model):
    
    class Meta():
        verbose_name_plural = 'Galleries'

    name = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    

class GalleryItemCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    gallery = models.ForeignKey(Gallery)
    title = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    description = models.TextField()
    category = models.ForeignKey(GalleryItemCategory, null=True, blank=True)

    def __str__(self):
        return self.title
