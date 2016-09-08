from django.conf.urls import url
from .views import index_page_view, post_view, blog_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index_page_view, name='index_view'),
    url(r'^blog/page/(?P<page>[0-9]+)/$', blog_view, name='blog_view'),
    url(r'^blog/post/(?P<pk>[0-9]+)/$', post_view, name='post_view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
