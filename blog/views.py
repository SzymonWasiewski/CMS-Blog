from .models import Post
from comments.forms import CommentForm
from comments.models import Comment, CommentReply
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect


# Index Page View
# HomePage
def index_page_view(request):
    posts = Post.objects.all()[:5]
    comment_count = []
    for post in posts:
        comment_count.append(Comment.objects.filter(post_id=post.id).count())
    n = int(5)
    context = {
        "title_page": "PythonKnowledge",
        "posts": posts,
        "comments": comment_count,
        "range": n,
    }

    return render(request, "blog/index.html", context)


# Post View
def post_view(request, pk=None):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post_id=pk)
    form = CommentForm(request.POST or None)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id_id = pk
            comment.save()
            return HttpResponseRedirect('/')

    return render(request, "blog/post.html", context)


# Blog View
# List of all Posts
def blog_view(request, page):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = page

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
    }

    return render(request, "blog/blog.html", context)
