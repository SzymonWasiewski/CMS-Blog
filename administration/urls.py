from django.conf.urls import url
from .views import (
    login_view, logout_view, error_page_view,
    administration_view,
    create_post_view, read_post_view, edit_post_view, delete_post_view,
    edit_authors_view, edit_author_view, delete_author_view,
    edit_comments_view, edit_comment_view, delete_comment_view,
)

urlpatterns = [
    # Login, Logout, Error URLS
    url(r'^login/$', login_view, name='login_view'),
    url(r'^logout/$', logout_view, name='logout_view'),
    url(r'^error/$', error_page_view, name='error_view'),
    # Panel URLS
    url(r'^panel/$', administration_view, name='administration_view'),
    # Panel/Post URLS
    url(r'^panel/create_post/$', create_post_view, name='create_post_view'),
    url(r'^panel/read_post/(?P<pk>[0-9]+)/$', read_post_view, name='read_post_view'),
    url(r'^panel/edit_post/(?P<pk>[0-9]+)/$', edit_post_view, name='edit_post_view'),
    url(r'^panel/delete_post/(?P<pk>[0-9]+)/$', delete_post_view, name='delete_post_view'),
    # Panel/Author URLS
    url(r'^panel/edit_authors/$', edit_authors_view, name='edit_authors_view'),
    url(r'^panel/edit_author/(?P<author_id>[0-9]+)/$', edit_author_view, name='edit_author_view'),
    url(r'^panel/delete_author/(?P<author_id>[0-9]+)/$', delete_author_view, name='delete_author'),
    # Panel/Comment URLS
    url(r'^panel/edit_comments/(?P<post_id>[0-9]+)/$', edit_comments_view, name='edit_comments_view'),
    url(r'^panel/edit_comment/(?P<comment_id>[0-9]+)/$', edit_comment_view, name='edit_comment_view'),
    url(r'^panel/delete_comment/(?P<comment_id>[0-9]+)/$', delete_comment_view, name='delete_comment_view'),
]
