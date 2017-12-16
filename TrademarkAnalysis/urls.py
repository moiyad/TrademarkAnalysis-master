from django.conf.urls import include, url
from django.conf.urls import url
from django.contrib import admin

from core import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^simple.search/', include('simpleSearch.urls')),

    url(r'^registration/', include('blog.urls')),

    url(r'^$', views.main_page, name='main_page'),
    url(r'^home/$', views.home, name='home'),
    url(r'^uploads_simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads_form/$', views.model_form_upload, name='model_form_upload'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
