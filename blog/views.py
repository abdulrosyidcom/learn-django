from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Halaman apa'
    }

    return render(request, 'blog/index.html', context)