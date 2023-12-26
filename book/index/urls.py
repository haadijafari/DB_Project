from django.urls import path
from index.views import *

app_name = 'index'

urlpatterns = [
    path('', index_view, name='index'),
    path('tag/<str:tag_name>', index_view, name='tag'),
    path('search/', search_view, name='search'),
    path('add/', new_book_view, name='new_book'),
]