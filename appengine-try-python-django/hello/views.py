from django import http

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
"""


def formatting_sample(request):
    s = 'The crappy persons name is %(suz)s and %(sup)s' % {"sup": "crappy", "suz": "crappppp"}
    print s
    return http.HttpResponse(s)