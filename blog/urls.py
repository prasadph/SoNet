from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', views.auth_login, name='login'),
    url(r'^blog/posts/new$', views.post, name='post'),
    url(r'^blog/posts/(?P<post_id>[0-9]+)/$', views.view_post, name='view_post'),
    url(r'^blog/tags/(?P<tag_id>[0-9]+)/$', views.posts_by_tag_id, name='posts_by_tag'),
    # url(r'^blog/tags/(?P<tag_id>[A-Za-z0-9]+)/$', views.posts_by_tag, name='posts_by_tag'),
]
