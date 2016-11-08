# -*- coding: utf-8 -*-

'''Entry point to all things to avoid circular imports.'''

from app import app, pages, freezer
from views import *


if __name__ == '__main__':

    app.run(debug=True, port=5000)
