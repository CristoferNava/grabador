from django.shortcuts import get_object_or_404, render
from .models import Article

def article(request, article_id, article_slug):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article': article})

def blog(request):
    blogs = Article.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blogs})
