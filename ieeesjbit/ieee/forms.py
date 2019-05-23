from django.forms import ModelForm
from .models import Posts


class Post(ModelForm):
    class Meta:
        model = Posts
        fields = ['Name', 'About_Post', 'Attachment']