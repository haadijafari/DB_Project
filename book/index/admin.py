from django.contrib import admin
from index.models import Book, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = (
        'name',
        'user',
        'author',
        'status',
        'age_group',
    )
    
    list_filter = ('status', 'category', 'user', 'author', 'tag')
    search_fields = ('name', 'author', )


admin.site.register(Category)
