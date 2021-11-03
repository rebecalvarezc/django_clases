from django.shortcuts import render
from .models import Post


# Create your views here.
def blog(request):
    post = Post.objects.all()
    return render(request, 'C:/Users/Rebeca/PycharmProjects/djangoProject/firstWeb/blogApp/templates/blog/blog.html',
                  {'posts': post})
