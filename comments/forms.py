from django import forms
from .models import Comment, CommentReply


# Comment Form - Add Comment to Post.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'email',
            'content',
        ]
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Nick'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'content': forms.Textarea(attrs={'placeholder': 'Comment...'}, ),
        }


# Comment Edit Form - Edit Comment or Approved it.
class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'id',
            'approved',
            'author',
            'email',
            'content',
        ]
