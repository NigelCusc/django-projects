from django.contrib import admin
from .models import Address, Author, Book, Country

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {
        "slug": ("title",)
    }
    # list_display = ("title", "author", "rating")
    list_filter = ("author", "rating", "is_bestselling")
    list_display = ("title", "author", "rating", "is_bestselling")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    prepopulated_fields = {
        "slug": ("name",)
    }

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)