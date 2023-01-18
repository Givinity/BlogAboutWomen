from django.http import HttpResponse


from django.shortcuts import render

from .models import *

stak = ['Python', 'Django', 'FastAPI']
def index(request):
    posts = Women.objects.all()
    return render(request, 'startpage/index.html', {'title': 'startpage', 'spisok': stak, 'posts': posts})
