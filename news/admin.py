from django.contrib import admin

from .models import NewsModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    fields = ['name', 'text', 'published', 'author',]

