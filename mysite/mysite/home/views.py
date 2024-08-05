from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape

# Create your views here.

def home(request, inp=None):
    # print(request)
    response = """
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title>Home</title>
          </head>
          <body>
            <h1>Hello, World!</h1>
            <p>Welcome to my application</p>
          </body>
        </html>
    """
    return HttpResponse(response)


def guessing(request, guess):
    # print(request.GET)
    response = """
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title>Home</title>
          </head>
          <body>
            <p>Your guess was {guess}</p>
          </body>
        </html>
    """.format(guess=guess)
    return HttpResponse(response)

def danger(request):
    print(request.GET['guess'])
    response = """
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title>Home</title>
          </head>
          <body>
            <p>Your guess was {guess}</p>
          </body>
        </html>
    """.format(guess=escape(request.GET['guess']))
    return HttpResponse(response)

def bounce(request):
    return HttpResponseRedirect("/home")
