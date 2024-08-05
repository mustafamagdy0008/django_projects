from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ArticleForm
from .models import Article

def article_search_view(request):
    print(request.GET)
    query_dict = request.GET
    query = query_dict.get("q")

    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request, "articles/search.html", context=context)


@login_required
def article_create_view(request, id=None):
    form = ArticleForm()
    # print(dir(form))
    # print("Form is: ", form)
    context = {
        "form": form
    }
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            # print(title, content)
            print("Cleaned Title: ", title)
            print("Cleaned Content: ", content)
            article_object = Article.objects.create(title=title, content=content)
            context['object'] = article_object
            context['created'] = True
    return render(request, "articles/create.html", context=context)



def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)
