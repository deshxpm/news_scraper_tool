from django.test import TestCase
import json

# Create your tests here.

scraping_pattern = {
    "article_selector": "div.article",
    "title_selector": "h2.title",
    "link_selector": "a",
    "image_selector": "img",
    "video_selector": "iframe",
    "category_selector": ".category",
    "author_selector": ".author",
    "date_selector": ".date"
}

pattern = scraping_pattern
print(pattern)