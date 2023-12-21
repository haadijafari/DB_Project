from django.contrib import admin
from index.models import Book, Category


@admin.register(Book)
class PortfolioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = (
        'name',
        'author',
        'status',
        'age_group',
        'created_date',
        'reading_date',
    )
    
    list_filter = ('status', 'category', 'created_date', 'reading_date', )
    search_fields = ('name', 'author', )


admin.site.register(Category)
