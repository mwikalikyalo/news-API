from unicodedata import category
from flask import render_template, Flask
from . import main
from ..request import get_articles

app= Flask(__name__)

@main.route('/')
def news():
    '''
    View sources page function that returns the articles from the source data
    '''
    article = get_articles()
    title = 'In the Headlines'
    return render_template('news.html', title = title, article = article)

# @main.route('/')
# def index():
#     '''
#     View root page function that returns the index page and its data
#     '''
#     news = get_news(category)
#     title = 'CNN'
#     return render_template('index.html', title = title, news = news)
   



