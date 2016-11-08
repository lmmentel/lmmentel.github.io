# -*- coding: utf-8 -*-

from flask import render_template
from app import app, pages


def get_posts():

    posts = [page for page in pages if 'date' in page.meta and
             page.meta.get('publish', True)]

    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
                          key=lambda page: page.meta['date'])

    return sorted_posts


@app.route('/')
def home():

    posts = get_posts()

    return render_template('index.html', pages=posts)


@app.route('/<path:path>/')
def page(path):

    # `path` is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@app.route('/news/')
def news():

    posts = get_posts()

    return render_template('news.html', pages=posts)
