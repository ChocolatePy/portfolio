from django.shortcuts import render

from .models import GalleryItem
from .models import Gallery

# Create your views here.
def gallery(request):
    items = GalleryItem.objects.filter(published=True)

    context = {
            'title': 'Fotos',
            'items': items,
    }

    return render(request, 'gallery/gallery.html', context)

