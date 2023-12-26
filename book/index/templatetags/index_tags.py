from django import template
from django.utils import timezone
from django.db.models import Count, Q
from index.models import Book, Category

register = template.Library()


@register.inclusion_tag('index/index-book-list.html')
def user_books(username):
    user_books = Book.objects.filter(user__username=username).order_by('-reading_date_end', '-status')

    return {'books': user_books, 'username': username}

@register.inclusion_tag('index/index-book-list-categories.html')
def user_post_categories(username):
    categories = Category.objects.filter(book__user__username=username).annotate(
        book_count=Count('book')
    ).order_by('-book_count')

    categories_dict = {cat.name: cat.book_count for cat in categories}

    return {'categories': categories_dict, 'all_cat_count': categories.count()}

@register.filter(name="compare_to_now")
def compare_to_now(value):
    now = timezone.now()
    return value < now