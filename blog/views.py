from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_main(request):
    posts = Blog.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blogs.html', context)


def detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})