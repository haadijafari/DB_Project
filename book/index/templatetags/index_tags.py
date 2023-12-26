from django import template
from django.utils import timezone
from django.db.models import Count
from index.models import Book, Category
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag('index/index-book-list.html')
def user_books(username, tag):
    user_books = Book.objects.filter(user__username=username).order_by(
        '-reading_date_end', '-status')
    if tag:
        user_books = user_books.filter(tag__name__in=[tag])

    return {'books': user_books, 'username': username}


@register.inclusion_tag('index/index-book-list-categories.html')
def user_post_categories(username):
    categories = Category.objects.filter(book__user__username=username).annotate(
        book_count=Count('book')
    ).order_by('-book_count')

    categories_dict = {cat.name: cat.book_count for cat in categories}
    all_count = Book.objects.filter(user__username=username).count()

    return {'categories': categories_dict, 'all_cat_count': all_count}


@register.filter(name="compare_to_now")
def compare_to_now(value):
    now = timezone.now()
    return value < now


@register.inclusion_tag('index/index-tags.html')
def user_tags(username):
    books = Book.objects.filter(user__username=username)
    tags = Tag.objects.filter(book__in=books).distinct()

    return {'tags': tags}
