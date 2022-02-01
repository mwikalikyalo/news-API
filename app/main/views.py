from flask import render_template, Flask
from app import main
from app.main import app
from main.config import DevConfig
from models.news import News

app= Flask(__name__)

# Views
@app.route('/')
def index():

    '''View root page function that returns the index page and its data'''
    return render_template('index.html')

@app.route('/home')
def index():
  '''View root page function that returns the home page and its data'''
  return render_template('home.html')

@main.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news= News(id)
    name = f'{news.name}'

    return render_template('news.html',name= name,news = news)

# Setting up configuration
app.config.from_object(DevConfig)

if __name__ == '__main__':
  app.run(debug=True)

from app.main import views