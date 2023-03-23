from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo',
                    'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('time_create',)
    prepopulated_fields = {'slug': ('title', )}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)