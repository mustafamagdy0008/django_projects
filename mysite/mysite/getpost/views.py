from django.shortcuts import render, redirect
from django.http import HttpResponse
import html
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.views import View

# Create your views here.

def dumpdata(place, data):
    retval = ""
    if len(data) > 0:
        retval += '<p>Incoming ' + place +' data<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' +html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

def getform(request):
    response = """<p>Impossible GET guessing game</p>
        <form>
            <p><label for="guess">Input Guess</label>
            <input type="text" name="guess" size="40" id="guess"></p>
            <input type="submit" >
        </form>
    """
    response += dumpdata('GET', request.GET)
    return HttpResponse(response)


@csrf_exempt
def postform(request):
    response = """<p>Impossible POST guessing game</p>
        <form method="POST">
            <p><label for="guess">Input Guess</label>
            <input type="text" name="guess" size="40" id="guess"></p>
            <input type="submit" >
        </form>
    """
    response += dumpdata('POST', request.POST)
    return HttpResponse(response)

def csrfform(request):
    response = """<p>CSRF Success guess game...</p>
        <form method="POST">
            <p><label for="guess">Input Guess</label>
            <input type="text" name="guess" size="40" id="guess"></p>
            <input type="hidden" name="csrfmiddlewaretoken" value="__token__" >
            <input type="submit" >
        </form>
    """
    token = get_token(request)
    response = response.replace('__token__', token)
    response += dumpdata('POST', request.POST)
    return HttpResponse(response)


def checkguess(guess):
    msg = False
    try:
        if int(guess) < 42:
            msg = 'Guess too low'
        elif int(guess) > 42:
            msg = 'Guess too high'
        else:
            msg = 'Congratulations!'
    except:
        msg = 'Bad format for guess:  ' + html.escape(guess)
    return msg


class ClassView(View):
    def get(self, request):
        return render(request, 'getpost/guess.html', {})

    def post(self, request):
        guess = request.POST.get('guess')
        print(guess)
        msg = checkguess(guess)
        print(msg)
        return render(request, 'getpost/guess.html', {'message': msg})


class AwesomeView(View):
    def get(self, request):
        msg = request.session.get('msg', False)
        if (msg) : del (request.session['msg'])
        return render(request, 'getpost/guess.html', {'message': msg})

    def post(self, request):
        guess = request.POST.get('guess')
        msg = checkguess(guess)
        request.session['msg'] = msg
        return redirect(request.path)


class Login(View):
    def get(self, request):
        return render(request, 'getpost/login.html', {})
        
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('pass')
        return render(request, 'getpost/login.html', {})
