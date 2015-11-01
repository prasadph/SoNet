from django.contrib import admin
from .models import Post, Comment, Tag, Vote, TagsPosts


admin.site.register(Comment)

admin.site.register(Vote)
admin.site.register(TagsPosts)


class AddTag(admin.StackedInline):
    model = TagsPosts
    extra = 3


class Posts(admin.ModelAdmin):
    model = Post
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['text']}),
        (None, {'fields': ['author']}),
    ]
    inlines = [AddTag]


admin.site.register(Tag)
admin.site.register(Post,Posts)