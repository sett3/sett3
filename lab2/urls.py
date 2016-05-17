from django.conf.urls import patterns, url

from django.contrib import admin

from lab2.views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', admin.site.urls)
)