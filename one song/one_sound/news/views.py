from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    news_list = News.objects.all().order_by('-published_date')
    return render(request, 'news.html', {'news_list': news_list})

def news_list(request):
    category = request.GET.get('category')
    if category:
        news_list = News.objects.filter(category=category).order_by("-published_date")
    else:
        news_list = News.objects.all().order_by("-published_date")
    return render(request, 'news.html', {'news_list': news_list, 'selected_category': category})