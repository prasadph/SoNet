from django.contrib import admin
from .models import Post, Comment, Tag, Vote, Detail, TagsPosts

admin.site.register(Comment)
admin.site.register(Detail)
admin.site.register(Vote)


# admin.site.register(TagsPosts)


class AddTag(admin.StackedInline):
    model = TagsPosts
    extra = 1
    fieldsets = [(None, {'fields': ['tag']})]


class Posts(admin.ModelAdmin):
    model = Post
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['text']}),
        (None, {'fields': ['author']}),
    ]
    inlines = [AddTag]
    # filter_horizontal = [(None, {'fields': ['tag']})]


admin.site.register(Tag)
admin.site.register(Post, Posts)
