from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404

from .models import *

menu = [
    {'title': 'Главная страница', "url_name": 'home'},
    {'title': 'О сайте', "url_name": 'about'}
]
def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    return render(request, 'startpage/index.html', {'title': 'startpage', 'spisok': menu, 'posts': posts, 'cats': cats})

def about(request):
    return render(request, 'startpage/about.html')

def show_post(request, post_id):
    post = get_object_or_404(Women, pk=post_id)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'startpage/post.html')
def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    return render(request, 'startpage/index.html', {'title': 'startpage', 'spisok': menu,
                                                    'posts': posts, 'cat_id': cat_id})
