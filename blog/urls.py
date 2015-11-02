from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', views.auth_login, name='login'),
    url(r'^post/$', views.post, name='post'),
    url(r'^blog/post/(?P<post_id>[0-9]+)/$', views.view_post, name='view'),
]
