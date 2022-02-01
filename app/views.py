from flask import render_template, Flask
from app import app
from .config import DevConfig

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

# Setting up configuration
app.config.from_object(DevConfig)

if __name__ == '__main__':
  app.run(debug=True)

from app import views