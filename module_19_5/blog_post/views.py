from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}
    return render(request, 'blog_post_list.html', context)


def post_list_view(request):
    per_page = request.GET.get('per_page') or 2
    posts = Post.objects.all().order_by('-id') or per_page
    paginator = Paginator(posts, per_page)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}
    return render(request, 'blog_post_list_view.html', context)
