import logging
import datetime

from models import Greeting
from django import http, template
from django.template.loader import get_template
from django.template import Context
from google.appengine.api import memcache, users

from Calculator import *

"""

huge ass comments

hahaha


"""


def home(request):
    #im a comment
    print("Test Huge Ass Print")

    a = 300
    b = 200
    c = a * b

    if a > b:
        s = "A is Great"
    elif b > a:
        s = "B is Great"
    else:
        s = "I dont know who's greater..."

    print(s)

    for a in range(1, 10):
        scumbag(" aaa" + str(a), "bbb " + s + " " + str(c))

    list_sample()
    return http.HttpResponse(s)


def scumbag(p1, p2):
    print ("invoke the scumbag method" + p1 + " --- " + p2)


def list_sample():
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)
    my_dictionary = {'a': 1, 'b': 6}

    casted_to_list = list(my_tuple)

    print(my_tuple)
    print(my_list)
    print(casted_to_list)
    print(my_dictionary)
    return my_list

"""
trying out this stuff: https://docs.python.org/2/library/stdtypes.html#string-formatting
read on the appengine-specifics: https://developers.google.com/appengine/docs/python/requests
"""


def formatting_sample(request):
    #sample logging
    logging.error("testing debug log")

    calc = Calculator()
    calc.add(2)
    print("calculated:" + str(calc.get_current()))

    s = 'The crappy persons name is %(suz)s and %(sup)s' % {"sup": "crappy", "suz": "crappppp"}
    print s
    return http.HttpResponse(s)


def clock(request):
    r = "Time is "
    r += str(datetime.datetime.now())

    return http.HttpResponse(r)


# templates: http://www.djangobook.com/en/2.0/chapter04.html
def template_test(request):
    t = template.Template('My Name is {{name}}')
    c = template.Context({'name': 'Test'})

    return http.HttpResponse(t.render(c))


def template_file(request):
    #copied this from: https://developers.google.com/appengine/articles/django-nonrel
    user = users.get_current_user()

    g1 = Greeting()
    g1.author = user
    g1.content = "Whatever"

    context = {
        'user': user,
        'greetings': [g1],
        'login': '/login',
        'logout': '/logout',
    }

    t = get_template('index.html')
    return http.HttpResponse(t.render(Context(context)))