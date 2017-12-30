from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [


    url(r'^$', views.main_page, name='home'),
    url(r'^uploads_simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads_form/$', views.model_form_upload, name='model_form_upload'),
    # url(r'^admin/', admin.site.urls),

]