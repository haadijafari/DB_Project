from django import forms
from django.contrib.auth.models import User

from index.models import Book, Category


class BookForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select'}),
        required=False
    )
    
    user = forms.ModelChoiceField(
            queryset=User.objects.all(), widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Book
        fields = (
            'name',
            'isbn',
            'author',
            'age_group',
            'category',
            'tag',
            'reading_date_start',
            'reading_date_end',
            'status',
            'file',
            'page_num_for_cover',
        )
