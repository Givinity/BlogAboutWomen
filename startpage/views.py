from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddPostForm
from .models import *

menu = [
    {'title': 'Главная страница', "url_name": 'home'},
    {'title': 'О сайте', "url_name": 'about'},
    {'title': 'Добавить статью', "url_name": 'addpage'}
]
def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    return render(request, 'startpage/index.html', {'title': 'startpage', 'spisok': menu, 'posts': posts, 'cats': cats})

def about(request):
    return render(request, 'startpage/about.html')

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'startpage/post.html', context=context)
def show_category(request, cat_slug):
    posts = Women.objects.filter(cat__slug=cat_slug)
    context = {
        'title': 'startpage',
        'spisok': menu,
        'posts': posts,
        'cat_slug': cat_slug
    }

    return render(request, 'startpage/index.html', context=context)

def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'startpage/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})
