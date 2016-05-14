from django.conf.urls import url
from rest_api import views

urlpatterns = [
    url(r'^apps/$', views.AppList.as_view(), name='apps'),
    url(r'^repos/$', views.RepoList.as_view(), name='repos'),
    url(r'^articles/$', views.ArticleList.as_view(), name='articles'),
]
