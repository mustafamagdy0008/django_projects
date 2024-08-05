"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request, id=None):
    """
    Take in a request (Django sends the request)
    Return HTML as a response (We pick to return the response)
    """
    rand_id = random.randint(1, 3)
    article_obj = Article.objects.get(id=rand_id)

    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content
    }
    HTML_STRING = render_to_string('home-view.html', context=context)
    return HttpResponse(HTML_STRING)