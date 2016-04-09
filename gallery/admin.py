from django.contrib import admin

from .models import Gallery
from .models import GalleryItem
from .models import GalleryItemCategory


class GalleryItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'gallery',
        'published',
    )
    list_filter = ('category', 'gallery', 'published')

# Register your models here.
admin.site.register(Gallery)
admin.site.register(GalleryItem, GalleryItemAdmin)
admin.site.register(GalleryItemCategory)

