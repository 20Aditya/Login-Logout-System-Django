from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='form'),
    url(r'^new/$', views.new_account, name='new_account'),
    url(r'^login/$', views.newloginView.as_view(), name='login'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^loggedout/$', views.user_logout, name='loggedout'),
    url(r'^invalid/$', views.invalid_login, name='invalid'),
]