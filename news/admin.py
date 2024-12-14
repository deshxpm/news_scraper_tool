from django.contrib import admin
from .models import NewsSource, NewsArticle

@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_url')
    search_fields = ('name',)
    ordering = ('name',)  # Orders sources alphabetically by name

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'published_at', 'is_scraped', 'view_link')
    search_fields = ('title',)
    list_filter = ('source', 'is_scraped', 'published_at')
    ordering = ('-published_at',)  # Orders articles by most recent publication date
    date_hierarchy = 'published_at'  # Adds navigation by published date

    def view_link(self, obj):
        """Creates a clickable link to the article"""
        return f'<a href="{obj.link}" target="_blank">View Article</a>'
    view_link.allow_tags = True
    view_link.short_description = "Article Link"
