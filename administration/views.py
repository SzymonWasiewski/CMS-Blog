from django.contrib.auth import authenticate, login, logout
from django.views.decorators.debug import sensitive_post_parameters
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import UserLoginForm, PostForm, AuthorForm
from comments.forms import CommentEditForm

from blog.models import Post, Author
from comments.models import Comment


# Login View
@sensitive_post_parameters(
    'username',
    'password',
)
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/administration/panel/')
    return render(request, "administration/login.html", {"form": form})


# Logout View
def logout_view(request):
    logout(request)
    return render(request, "administration/logout.html")


# Error Page View
def error_page_view(request):
    return render(request, "administration/error_page.html")


# Administration View
def administration_view(request):
    if not request.user.is_authenticated():
        return render(request, "administration/error_page.html")
    else:
        posts = Post.objects.all()
        comments = Comment.objects.all()
        context = {
            "posts": posts,
            "comments": comments,
        }
        return render(request, "administration/administration.html", context)


# Create Post View
def create_post_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/administration/login/')
    else:
        form = PostForm(request.POST or None)
        image = request.POST.get('image')
        if form.is_valid():
            post = form.save(commit=False)
            post.image = image
            post.save()
            return HttpResponseRedirect('/administration/panel/')
        context = {
            "form": form,
        }
        return render(request, "administration/create_post.html", context)


    # Edit Post View:
    # Single Post


def edit_post_view(request, pk=None):
    if not request.user.is_authenticated():
        return render(request, "administration/error_page.html")
    else:
        post = get_object_or_404(Post, id=pk)
        form = PostForm(request.POST or None, instance=post)
        image = request.POST.get('image')
        if form.is_valid():
            post.image = image
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect("/administration/panel/")
        context = {
            "post": post,
            "form": form,
        }
        return render(request, "administration/edit_post.html", context)


# Delete Post View
def delete_post_view(request, pk=None):
    if not request.user.is_authenticated():
        return render(request, "administration/error_page.html")
    else:
        post = get_object_or_404(Post, id=pk)
        post.delete()
        return HttpResponseRedirect("/administration/panel/")


# Read Post View
def read_post_view(request, pk=None):
    if not request.user.is_authenticated():
        return render(request, "administration/error_page.html")
    else:
        post = get_object_or_404(Post, id=pk)
        comments = Comment.objects.filter(post_id=pk)
        context = {
            "post": post,
            "comments": comments,
        }
        return render(request, "administration/post.html", context)


    # Edit Authors View
    # Add Author
    # List of Authors to Edit
def edit_authors_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/administration/login')
    else:
        authors = Author.objects.all()
        form = AuthorForm(request.POST or None)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return HttpResponseRedirect('/administration/panel/')
        context = {
            "authors": authors,
            "form": form,
        }
        return render(request, "administration/edit_authors.html", context)


# Delete Author View
def delete_author_view(request, author_id):
    if not request.user.is_authenticated():
        return render(request, "administration/error_page.html")
    else:
        author = get_object_or_404(Author, id=author_id)
        author.delete()
        return HttpResponseRedirect("/administration/")


    # Edit Author View
    # Single Author
def edit_author_view(request, author_id=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/administration/login')
    else:
        author = get_object_or_404(Author, id=author_id)
        form = AuthorForm(request.POST or None, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return HttpResponseRedirect("/administration/panel/")

        context = {
            "author": author,
            "form": form,
        }
        return render(request, "administration/edit_author.html", context)


    # Edit Comments View
    # List of Comments from Single Post to Edit


def edit_comments_view(request, post_id=None):
    if not request.user.is_authenticated():
        return render(request, "administration/error_page.html")
    else:
        comments = Comment.objects.filter(post_id=post_id)
        context = {
            "comments": comments,
        }
    return render(request, "administration/edit_comments.html", context)


# Edit Comment View
# Single Comment
def edit_comment_view(request, comment_id=None):
    if not request.user.is_authenticated():
        return render(request, "administration/error_page.html")
    else:
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentEditForm(request.POST or None, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return HttpResponseRedirect("/administration/panel/")
        context = {
            "comment": comment,
            "form": form,
        }
        return render(request, "administration/edit_comment.html", context)


# Delete Comment View
def delete_comment_view(request, comment_id=None):
    if not request.user.is_authenticated():
        return render(request, "administration/error_page.html")
    else:
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return HttpResponseRedirect("/administration/panel/")
