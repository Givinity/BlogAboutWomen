from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [
    {'title': 'Главная страница', "url_name": 'home'},
    {'title': 'О сайте', "url_name": 'about'},
    {'title': 'Добавить статью', "url_name": 'addpage'},
    {'title': 'Обратная связь', "url_name": 'contact'},
]

class DataMixin:
    paginate_by = 2



    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('women'))
            cache.set('cats', cats, 60)

        menu_copy = menu.copy()
        if not self.request.user.is_authenticated:
            menu_copy.pop(2)
        context['spisok'] = menu_copy
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
