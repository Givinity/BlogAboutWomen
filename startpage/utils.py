from .models import *

menu = [
    {'title': 'Главная страница', "url_name": 'home'},
    {'title': 'О сайте', "url_name": 'about'},
    {'title': 'Добавить статью', "url_name": 'addpage'}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['spisok'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
