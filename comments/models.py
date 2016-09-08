from django.db import models
from blog.models import Post


class Comment(models.Model):
    post_id = models.ForeignKey(Post)
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=1000)
    author = models.CharField(max_length=64)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = ['Comments']
        ordering = ['-date']

    def __str__(self):
        return u'%s' % self.content


class CommentReply(models.Model):
    post_id = models.ForeignKey(Comment)
    content = models.CharField(max_length=256)
    author = models.CharField(max_length=64)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = ['Comment Replies']
        ordering = ['-date']

    def __str__(self):
        return u'%s' % self.content
