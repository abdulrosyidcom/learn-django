from django.shortcuts import render

def home(request):
    context = {
        'title': 'Halaman Home'
    }
    return render(request, 'home/index.html', context)