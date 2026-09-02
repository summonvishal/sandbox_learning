from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter blog title...',
                'class': 'form-input'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your blog content here...',
                'rows': 5,
                'class': 'form-input'
            }),
        }
