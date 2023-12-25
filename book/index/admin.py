from django.contrib import admin
from index.models import Book, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = (
        'name',
        'author',
        'status',
        'age_group',
        'created_date',
        'reading_date_start',
        'reading_date_end',
    )
    
    list_filter = ('status', 'category', 'reading_date_start', 'reading_date_end', )
    search_fields = ('name', 'author', )


admin.site.register(Category)
