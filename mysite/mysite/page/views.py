from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def lessons(request):
    response = """
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title>Home</title>
          </head>
          <body>
            <h1>Simple Page</h1>
            <p>Some cool online <a href='/bounce'>lesson</a> </p>
          </body>
        </html>
        """
    return HttpResponse(response)

def bounce(request):
    return HttpResponseRedirect("https://docs.djangoproject.com/en/5.0/")
