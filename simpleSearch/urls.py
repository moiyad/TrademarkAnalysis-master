from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^simpleSearch/$', views.search, name='search'),
    url(r'^searchResult/$', views.search_result),
]
