from django import template
from index.models import Book, Category

register = template.Library()

@register.inclusion_tag('index/index-book-list.html')
def all_books():
    books = Book.objects.all()
    # categories = Category.objects.all()
    return {'books': books}

@register.inclusion_tag('index/index-book-list-categories.html')
def post_categories():
    books = Book.objects.all()
    categories = Category.objects.all()
    cat_dict = {}
    for cat in categories:
        cat_dict[cat] = books.filter(category__name=cat.name).count()

    sorted_cat_dict = dict(
        sorted(cat_dict.items(), key=lambda item: item[1], reverse=True))
    return {'categories': sorted_cat_dict}