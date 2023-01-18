from django.http import HttpResponse


from django.shortcuts import render

from .models import *

menu = [
    {'title': 'Главная страница', "url_name": 'home'},
    {'title': 'О сайте', "url_name": 'about'}
]
def index(request):
    posts = Women.objects.all()
    return render(request, 'startpage/index.html', {'title': 'startpage', 'spisok': menu, 'posts': posts})

def about(request):
    return render(request, 'startpage/about.html')

def show_post(request, post_id):
    return HttpResponse(f'Отображается пост с id {post_id}')
