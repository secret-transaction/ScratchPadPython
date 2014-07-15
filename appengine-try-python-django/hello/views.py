from django import http

'''

huge ass comments

hahaha


'''
def home(request):
    #im a comment
    print("Test Huge Ass Print")

    a = 300
    b = 200
    c = a * b

    s = "Who is the greatest???"
    if a > b:
        s = "A is Great"
    elif b > a:
        s = "B is Great"
    else:
        s = "I dont know who's greater..."

    print(s)

    return http.HttpResponse(s)
