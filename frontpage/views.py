from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from models import AboutMe, Shop, Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    aboutme = AboutMe.objects.all()[:1]
    items = Shop.objects.all()
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(blogs, 3)
    page = request.GET.get('article')
    try:
      articles = (paginator.page(page))
    except PageNotAnInteger: 
      articles = paginator.page(1)
    except EmptyPage:
      articles = paginator.page(paginator.num_pages)
    template = 'index.html'
    return render(request, template, {'aboutme': aboutme, 'items':items, 'articles': articles} )