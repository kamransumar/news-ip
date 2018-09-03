from flask import render_template
from app import app
from .request import get_url, get_articles

# Views


@app.route('/')
def index():

    # Getting news source
    popular_sources = get_url()
    print(popular_sources)
    title = 'News Junction'
    sources = popular_sources

    return render_template('index.html', title=title, popular=sources)


@app.route('/article/<id>')
def articles(id):

    # Getting news articles
    popular_articles = get_articles(id)
    print(popular_articles)
    articles = popular_articles

    return render_template('index.html', popular=articles, id=id)
