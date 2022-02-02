from concurrent.futures import process
from unicodedata import category
from app.main import app
import urllib.request,json
import news
from news import News,Article

News = news.News

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain headlines

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('headline')
        tagline = news_item.get('tagline')
        link= news_item.get('links')
        languages= news_item.get('languages')

        if link:
            news_object = News(id,name,tagline,link,languages)
            news_results.append(news_object)

    return news_results


def get_articles(id):
    get_article_details_url = base_url.format(id,api_key)
    print(get_article_details_url)
    with urllib.request.urlopen(get_article_details_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        source_articles = get_articles_response

        if get_articles_response['articles']:
            source_articles_list = get_articles_response['articles']
            source_articles = process_articles(source_articles_list)
    return source_articles

def process_articles(articles):
    '''
    Function that processes the json results and returns a list of objects for the articles
    '''
    source_articles = []
    for article in articles:
        id = article.get('id')
        name = article.get('name')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        if url:
            article_object = Article(id, name, author, title,description, url, urlToImage, publishedAt, content)
            source_articles.append(article_object)

    return source_articles