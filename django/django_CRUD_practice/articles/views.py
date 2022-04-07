from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-id')

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.id)
    
        return redirect('articles:new')
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article':article,
    }

    return render(request, 'articles/detail.html', context)

def delete(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.id)

def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }

    return render(request, 'articles/update.html', context)
