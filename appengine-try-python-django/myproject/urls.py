from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'hello.views.formatting_sample'),
)
