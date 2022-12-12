from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['pizza','comment_text']
        labels = {'pizza':'Pizza Name','comment_text':''}
        widgets = {'comment_text': forms.Textarea(attrs={'cols':100,'rows':5})}