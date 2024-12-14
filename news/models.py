from django.db import models

class NewsSource(models.Model):
    name = models.CharField(max_length=100, unique=True)
    base_url = models.URLField(unique=True)
    scraping_pattern = models.TextField(help_text="CSS selectors for title and link in JSON format")

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    link = models.URLField()
    image_url = models.URLField(null=True, blank=True)  # Optional field for images
    video_url = models.URLField(null=True, blank=True)  # Optional field for videos
    category = models.CharField(max_length=100, null=True, blank=True)  # News category (e.g., Technology, Sports)
    author = models.CharField(max_length=100, null=True, blank=True)  # Article author
    published_date = models.DateTimeField(null=True, blank=True)  # Published date
    published_at = models.DateTimeField(auto_now_add=True)
    is_scraped = models.BooleanField(default=True)

    def __str__(self):
        return self.title
