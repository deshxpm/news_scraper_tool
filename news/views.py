from django.shortcuts import render
from .scraper import *
from django.http import JsonResponse

def scrape_and_display_news(request):
    source = NewsSource.objects.all()
    articles = NewsArticle.objects.all().order_by('-id')
    return render(request, 'news_scraper/news_list.html', {'articles': articles, 'sources':source})

def refresh_news(request):
    source_id = request.GET.get('source')
    if source_id:
        scrape_news(source_id)
        articles = NewsArticle.objects.filter(source_id=source_id)
        # Serialize the articles into JSON-friendly data
        serialized_articles = [
            {
                "title": article.title,
                "link": article.link,
                "image_url": article.image_url,
                "video_url": article.video_url,
                "source": {"name": article.source.name},
                "category": article.category,
                "author": article.author,
                "published_date": article.published_date.strftime('%Y-%m-%d %H:%M:%S') if article.published_date else None,
            }
            for article in articles
        ]
    else:
        serialized_articles = []

    return JsonResponse({'articles': serialized_articles})