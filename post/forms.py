from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    #meta class is used to directly take entry of a form to given models
    class Meta():
        model=Post
        fields=('title','des')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].label = 'Post Title'
        self.fields['des'].label = "Content"
