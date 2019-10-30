from django.conf.urls import url

from snippets import views

urlpatterns = [
    url(r'^snippet_list/$', views.snippet_list),
    url(r'^snippet_detail/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

