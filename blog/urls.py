from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list,name='post_list'),
    url(r'^login/$',views.auth_login,name='login'),
    url(r'^post/$',views.post,name='post')
]
