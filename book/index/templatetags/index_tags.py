from django import template
from index.models import Book, Category
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('index/index-book-list.html')
def all_books():
    books = Book.objects.all().order_by('-status')
    return {'books': books}

@register.inclusion_tag('index/index-book-list-categories.html')
def post_categories():
    books = Book.objects.all()
    categories = Category.objects.all()
    cat_dict = {}
    all = categories.count()
    for cat in categories:
        cat_dict[cat] = books.filter(category__name=cat.name).count()

    sorted_cat_dict = dict(
        sorted(cat_dict.items(), key=lambda item: item[1], reverse=True))
    return {'categories': sorted_cat_dict, 'all_cat_count': all}

@register.filter(name="compare_to_now")
def compare_to_now(value):
    now = timezone.now()
    return value < now