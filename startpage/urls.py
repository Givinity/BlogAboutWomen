from django.urls import path
from django.views.decorators.cache import cache_page
from startpage.views import *


urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='cat'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('contact/', ContactFormViev.as_view(), name='contact'),
]