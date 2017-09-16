from django.conf.urls import url
from django.contrib.auth import views as av
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'login/$',
        av.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),

    url(r'logout/$',
        av.LogoutView.as_view(),
        name='logout'),

    url(r'singup/$',
        views.Singup.as_view(),
        name='singup'),


]