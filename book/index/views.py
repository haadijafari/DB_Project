from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q

from index.forms import BookForm
from index.models import Category, Book


def index_view(request, **kwargs):
    return render(request, 'index/index.html', {'tag': kwargs.get('tag_name')})


@login_required
def new_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            # Save the form with the user
            book = form.save(commit=False)
            book.user = user
            book.save()
            # Without this next line the tags won't be saved.
            form.save_m2m()
        else:
            messages.error(request, 'Error while uploading book')

        return redirect('index:index')
    else:
        form = BookForm()
        categories = Category.objects.all()
        return render(request, 'index/index-add-book.html', {'form': form, 'categories': categories})

@login_required
def search_view(request):
    books = Book.objects.filter(user__username=request.user.username)
    if request.method == 'GET':
        if s := request.GET.get('search'):
            books = Book.objects.filter(
                Q(name__icontains=s) | Q(author__icontains=s) | Q(
                    isbn__icontains=s)
            )
            
            return render(request, 'index/index.html', {'books': books})