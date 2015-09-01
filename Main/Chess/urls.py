from django.conf.urls import url
from django.http import HttpResponseRedirect
from .views import ProfileView

urlpatterns = [
    url(r'^profile/$', ProfileView.as_view(), name="profile"),
]
