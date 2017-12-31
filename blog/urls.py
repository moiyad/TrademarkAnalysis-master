from django.conf.urls import include, url

from blog import views

urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'^login$', views.login, name='login'),
    url(r'^business_company$', views.user, {'template': 'business_company.html'}, name='business_company'),
    url(r'^guest_user$', views.user, {'template': 'guest_user.html'}, name='guest_user'),
    url(r'^law_firm$', views.user, {'template': 'law_firm.html'}, name='law_firm'),
    url(r'^success', views.success, name='success'),

]
