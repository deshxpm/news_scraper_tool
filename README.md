# news_scraper_tool
A dynamic news scraping platform displaying real-time articles from various sources.


# Project Overview:
This project is a news scraping and display platform that allows users to fetch and view the latest news articles from various sources. The tool uses web scraping techniques to extract news content and displays it in an organized manner, including images, videos, and article details. It features dynamic source selection, allowing users to choose a news provider, and refresh the feed to retrieve the latest articles.

# Technologies Used:

1. Python:
The backend is built using Python, leveraging popular libraries like requests for HTTP requests and BeautifulSoup for parsing and extracting data from web pages.
Django is used for building the web application, handling the routing, views, and serving dynamic content.

2. Web Scraping:
BeautifulSoup: A Python library for parsing HTML and XML documents. It’s used to scrape content from various news websites by extracting relevant information (e.g., titles, links, images, videos).
Requests: A Python HTTP library used to make network requests to fetch HTML content from news websites.

3. Frontend:
HTML: Used for structuring the web pages and displaying scraped news content.
Bootstrap 5: A CSS framework used to create a responsive and user-friendly layout for displaying articles and other content.
JavaScript/jQuery: Used for making AJAX requests to refresh the news feed dynamically without reloading the page.
CSS: Custom styling for improving the look and feel of the web pages, including responsive design elements.

4. Django:
Django serves as the backend framework to handle HTTP requests and responses, manage data, and render HTML templates.
Models: Django models are used to store scraped articles in a database for efficient access and management.
JsonResponse: Used to return the scraped articles as JSON data to the frontend for dynamic content updating.

5. Database:
SQLite/PostgreSQL: Used to store the scraped news articles, allowing for persistence across sessions and enabling easy retrieval and management of data.

6. AJAX:
JavaScript and AJAX are used to fetch and update the articles without reloading the entire page, providing a smooth user experience.

7. Django Templates:
Used to render dynamic HTML pages with the latest scraped articles, ensuring that the page content is updated based on the data stored in the backend.
