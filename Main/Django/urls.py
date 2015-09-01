"""Chess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.core.urlresolvers import reverse_lazy
from Chess.auth_views import RegisterView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/login/$', auth_view.login, name="login"),
    url(r'accounts/logout/$', auth_view.logout, {"next_page": reverse_lazy('login')}, name="logout"),
    url(r'register/', RegisterView.as_view(), name="register"),
    #chess app
    url(r'^chess/', include('Chess.urls', namespace="chess")),
]
