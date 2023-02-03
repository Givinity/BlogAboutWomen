from django.urls import path

from startpage.views import *


urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', WomenCategory.as_view(), name='cat'),
    path('addpage', AddPage.as_view(), name='addpage'),
]