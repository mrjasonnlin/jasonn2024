from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'like': 'Django 很棒'}
    return render(request, 'render/index.html', context)
