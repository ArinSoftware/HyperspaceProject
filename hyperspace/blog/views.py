from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog

def post_list(request):
    posts = Blog.objects.all()

    paginator = Paginator(posts, 1) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'posts': posts, "page_obj": page_obj})

def post_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
