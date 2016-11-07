# -*- coding: utf-8 -*-

from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

pages = FlatPages(app)
freezer = Freezer(app)
