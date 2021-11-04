from django.shortcuts import render
from .models import Post, Categories


# Create your views here.
def blog(request):
    post = Post.objects.all()
    return render(request, 'blog/blog.html',
                  {'posts': post})


def category(request, category_id):
    cat = Categories.objects.get(id=category_id)
    posts = Post.objects.filter(categories=cat)
    return render(request,
                  'blog/categories.html',
                  {'categories': cat, 'posts': posts})
