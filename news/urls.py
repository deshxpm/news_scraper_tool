from django.urls import path
from .views import scrape_and_display_news, refresh_news

urlpatterns = [
    path('', scrape_and_display_news, name='scrape-news'),
    path('refresh-news/', refresh_news, name='refresh-news'),
]
