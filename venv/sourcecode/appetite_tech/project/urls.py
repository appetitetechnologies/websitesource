from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^home/',views.home,name='home'),
    url(r'^projectlist/(?P<id>\d+)/$',views.projectlist,name='projectlist'),
    url(r'^projectdetail/(?P<id>\d+)/$',views.projectdetail,name='projectdetail'),
    url(r'^create/',views.ProjectCreate,name='projectcreate'),
]
