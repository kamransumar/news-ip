from flask import render_template
from app import app
from .request import get_url

# Views


@app.route('/')
def index():

    # Getting news source
    popular_sources = get_url()
    print(popular_sources)
    title = 'News Junction'

    return render_template('index.html', title=title, popular=popular_sources)
