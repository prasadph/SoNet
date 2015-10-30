from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post)
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Vote(models.Model):
    author = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post)
    TYPES = (
        ('U', 'Upvote'),
        ('D', 'Downvote'),
    )
    _type = models.CharField(max_length=1,choices=TYPES)

    def __str__(self):
        return self._type
