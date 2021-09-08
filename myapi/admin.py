from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Category, CategoryAdmin)


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('authors',)
    list_display = ('title', 'category',)
    list_filter = ('category', 'authors',)
    search_fields = ('title',)


admin.site.register(models.Book, BookAdmin)
