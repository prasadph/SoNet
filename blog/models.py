from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def validate_tag(value):
    if not value.isalnum():
        raise ValidationError('%s is not' % value)


class Detail(models.Model):
    user = models.OneToOneField('auth.User')
    address = models.CharField(max_length=200, default="")
    # dob = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, validators=[validate_tag])
    info = models.CharField(max_length=200)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_posts(self):
        return TagsPosts.objects.filter(tag=self)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField(Tag, through="TagsPosts", through_fields=("post", "tag"))

    def __str__(self):
        return self.title

    def get_votes(self):
        return Vote.objects.filter(post=self).count()

    def get_comments(self):
        return Comment.objects.filter(post=self)

    def get_tags(self):
        return Tag.objects.filter(tagsposts__post=self)


class TagsPosts(models.Model):
    class Meta:
        unique_together = ('post', 'tag')

    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)

    # created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "'{0}' '{1}'".format(self.post.title, self.tag.name)


class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post)
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


class Vote(models.Model):
    class Meta:
        unique_together = ('post', 'author')

    author = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post)
    TYPES = (
        ('U', 'Up vote'),
        ('D', 'Down vote'),
    )
    _type = models.CharField(max_length=1, choices=TYPES)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author.__str__() + " " + self._type
