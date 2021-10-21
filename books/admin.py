from django.contrib import admin

from .models import Book,Reveiew

class ReviewInline(admin.TabularInline):
    model = Reveiew


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title","author","price",)

admin.site.register(Book,BookAdmin)
