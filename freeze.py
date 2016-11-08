# -*- coding: utf-8 -*-

import os
import sys

p = os.path.join(os.getcwd(), 'flask-homepage')
sys.path.insert(0, p)

from project import main

if __name__ == '__main__':
    main.freezer.freeze()
