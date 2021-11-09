from django.shortcuts import render
from .models import Post, Categories


# Create your views here.
def blog(request):
    post = Post.objects.all()
    cat = [i.categories.all()[0] for i in post]
    cat = list(set(cat))
    return render(request, 'blog/blog.html',
                  {'posts': post, 'categories': cat})


def category(request, category_id):
    cat = Categories.objects.get(id=category_id)
    posts = Post.objects.filter(categories=cat)
    print(cat)
    return render(request,
                  'blog/categories.html',
                  {'categories': cat, 'posts': posts})
