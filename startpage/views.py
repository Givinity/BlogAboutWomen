from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import *
from .utils import *

class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'startpage/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    def get_queryset(self):
        return Women.objects.filter(is_published=True)

#def index(request):
#    posts = Women.objects.all()
#    cats = Category.objects.all()
#    return render(request, 'startpage/index.html', {'title': 'startpage', 'spisok': menu, 'posts': posts, 'cats': cats})

def about(request):
    return render(request, 'startpage/about.html')

class ShowPost(DetailView):
    model = Women
    template_name = 'startpage/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        context['cats'] = Category.objects.all()
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'startpage/post.html', context=context)

class WomenCategory(ListView):
    model = Women
    template_name = 'startpage/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                    is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория -' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context
# def show_category(request, cat_slug):
#     posts = Women.objects.filter(cat__slug=cat_slug)
#     context = {
#         'title': 'startpage',
#         'spisok': menu,
#         'posts': posts,
#         'cat_slug': cat_slug
#     }

#    return render(request, 'startpage/index.html', context=context)

# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = AddPostForm()
#     return render(request, 'startpage/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'startpage/addpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['spisok'] = menu
        return context