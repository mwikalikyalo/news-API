from flask import render_template, Flask
from . import main
from ..request import get_news


app= Flask(__name__)

# Views
@main.route('/')
def index():

    '''View root page function that returns the index page and its data'''
    return render_template('index.html')


@main.route('/news/<int:id>')
def news(id):
    '''
    View news page function that returns the news details page and its data
    '''
    news= get_news(id)
    name = f'{news.name}'

    return render_template('news.html',name= name,news = news)
   
   




