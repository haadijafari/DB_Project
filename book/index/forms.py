from django import forms

from index.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'name',
            'isbn',
            'author',
            'age_group',
            'category',
            'tag',
            'reading_date',
            'status',
            'file',
            'page_num_for_cover',
        )
