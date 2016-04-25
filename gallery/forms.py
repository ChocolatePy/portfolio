from django.forms import ModelForm

from .models import GalleryItemComment

class GalleryItemCommentForm(ModelForm):
    class Meta:
        model = GalleryItemComment
        fields = ['item', 'name', 'comment', 'date_time']
