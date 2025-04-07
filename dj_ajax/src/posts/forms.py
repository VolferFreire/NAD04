from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if not title:
    #         raise forms.ValidationError("Title is required.")
    #     return title

    # def clean_body(self):
    #     body = self.cleaned_data.get('body')
    #     if not body:
    #         raise forms.ValidationError("Body is required.")
    #     return body