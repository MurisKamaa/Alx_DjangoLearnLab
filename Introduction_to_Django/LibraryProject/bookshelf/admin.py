from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns in list view
    list_filter = ('publication_year', 'author')           # filters in right sidebar
    search_fields = ('title', 'author')                    # search box

# Register model with its custom admin class
admin.site.register(Book, BookAdmin)

