from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import GalleryItem
from .models import GalleryItemComment
from .models import Gallery

from .forms import GalleryItemCommentForm

# Create your views here.
def gallery(request):
    items = GalleryItem.objects.filter(published=True)

    context = {
            'title': 'Fotos',
            'items': items,
    }

    return render(request, 'gallery/gallery.html', context)

def gallery_item(request, item_id):
    item = get_object_or_404(GalleryItem, pk=item_id)

    context = {
            'item': item
    }
    return render(request, 'gallery/item.html', context=context)

def gallery_item_comment(request):
    
    form = GalleryItemCommentForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)

    context = {
            'form': form,
    }

    return render(request, 'gallery/gallery_item_comment.html', context)





# doing same thing manually
# def gallery_item(request, item_id):
    # try:
        # item = GalleryItem.objects.get(pk=item_id)
    # except GalleryItem.DoesNotExist:
        # raise Http404('nigga viado')

    # return render(request, 'gallery/item.html', {'item': item})
