from django.urls import path
from index.views import *

app_name = 'index'

urlpatterns = [
    path('', index_view, name='index'),
]