from django.conf.urls import *
from hello.views import *

urlpatterns = patterns(
    '',

    #home page
    url(r'^$', home),

    #note: r stands for 'raw' string (http://www.djangobook.com/en/2.0/chapter03.html)
    #access the formatting_sample view from: http://localhost:8080/formatting_sample/
    url(r'^formatting_sample/$', formatting_sample),

    url(r'^time/$', clock),

    # trying out templates
    url(r'^template/$', template_test),

    # using templates from file
    url(r'^template_file/$', template_file),
)
