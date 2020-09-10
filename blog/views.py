from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    context = {
        'title': 'Halaman apa',
        'Posts': Post.objects.all()
    }

    return render(request, 'blog/index.html', context)

def show(request, id):
    context = {
        'title': 'Detail Blog',
        'post': Post.objects.get(id=id)
    }

    return render(request, 'blog/show.html', context)
