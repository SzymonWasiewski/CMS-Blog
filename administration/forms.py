from blog.models import Post, Author
from django import forms
from django.contrib.auth import authenticate


# Login Form to Administration Panel
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Login',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
        }
    ))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User is not exist.")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("User is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)


# Post Form for Create or Edit Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'tags', 'content', 'author', 'image',
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                    'style': 'width: 40em;',
                }
            ),
            'tags': forms.TextInput(
                attrs={
                    'placeholder': 'Tags',
                    'style': 'width: 40em;',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Content',
                    'style': 'width: 40em; height: 30em;',
                }
            ),
            'author': forms.Select(
                attrs={
                    'placeholder': 'Author',
                    'style': 'width: 40em; ',
                }
            ),

        }


# Author Form for Create or Edit Author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'nick', 'email',
        ]
        widgets = {
            'nick': forms.TextInput(attrs={'placeholder': 'Nick'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }
