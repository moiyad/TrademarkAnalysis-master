from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.contrib import admin
from core import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^simple.search/', include('simpleSearch.urls')),


    url(r'^$', views.home, name='home'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




