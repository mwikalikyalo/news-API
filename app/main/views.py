from flask import render_template, Flask
from . import main
from ..request import get_news, get_article


app= Flask(__name__)

# Views
@main.route('/')
def so():

    '''View root page function that returns the index page and its data'''

    news = get_article()
    return render_template('source.html', news=news,)

@main.route('/news/<int:id>')
def news(id):
    '''
    View news page function that returns the news details page and its data
    '''
    news= get_news(id)
    name = f'{news.name}'

    return render_template('news.html',name= name,news = news)
   



