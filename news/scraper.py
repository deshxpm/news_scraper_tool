import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
from .models import NewsSource, NewsArticle
from datetime import datetime

def scrape_news(source_id):
    try:
        # Retrieve the news source object
        source = NewsSource.objects.get(id=source_id)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(source.base_url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        # Parse scraping pattern (stored as JSON)
        pattern = json.loads(source.scraping_pattern)
        articles = soup.select(pattern.get('article_selector', ''))

        news_list = []
        for article in articles:
            # Extract article details using CSS selectors
            title_tag = article.select_one(pattern.get('title_selector', ''))
            link_tag = article.select_one(pattern.get('link_selector', ''))
            image_tag = article.select_one(pattern.get('image_selector', ''))
            video_tag = article.select_one(pattern.get('video_selector', ''))
            category_tag = article.select_one(pattern.get('category_selector', ''))
            author_tag = article.select_one(pattern.get('author_selector', ''))
            date_tag = article.select_one(pattern.get('date_selector', ''))

            # Ensure we have a title and link to process the article
            if title_tag and link_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag['href']
                link = link if link.startswith('http') else urljoin(source.base_url, link)  # Handle relative links
                image_url = image_tag['src'] if image_tag else None
                image_url = image_url if image_url and image_url.startswith('http') else urljoin(source.base_url, image_url) if image_url else None
                video_url = video_tag['src'] if video_tag else None

                # Extract additional fields (category, author, published date)
                category = category_tag.get_text(strip=True) if category_tag else None
                author = author_tag.get_text(strip=True) if author_tag else None
                published_date = None
                if date_tag:
                    try:
                        # Parse the date, assuming it's in a recognizable format
                        published_date = datetime.strptime(date_tag.get_text(strip=True), "%Y-%m-%d")  # Example format: "2024-12-13"
                    except ValueError:
                        # Handle the case where the date format is unexpected
                        published_date = None

                # Save or get the news article
                article_obj, created = NewsArticle.objects.get_or_create(
                    source=source,
                    title=title,
                    link=link,
                    image_url=image_url,
                    video_url=video_url,
                    category=category,
                    author=author,
                    published_date=published_date
                )

                # Append to the list of news articles
                news_list.append(article_obj)

        return news_list
    except NewsSource.DoesNotExist:
        return f"NewsSource with ID {source_id} does not exist."
    except requests.exceptions.RequestException as e:
        return f"Request Error: {str(e)}"  # Handle HTTP errors
    except Exception as e:
        return f"Error: {str(e)}"  # Handle any other unforeseen errors


