from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cookie(request):
    print("COOKIES: ", request.COOKIES)
    response = HttpResponse("<p>C is for cookie that is good enough for me ...</p>")
    response.set_cookie('name', 'Mustafa')
    response.set_cookie('age', 20, max_age=20)
    return response

def sessfun(request):
    # print(request.session)
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    return HttpResponse(f'<p>view count = {num_visits}</p>')
