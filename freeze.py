# -*- coding: utf-8 -*-

import argparse
import os
import sys

p = os.path.join(os.getcwd(), 'flask_homepage')
sys.path.insert(0, p)

from flask_homepage import main

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--run', action="store_true")
    args = parser.parse_args()

    if args.run:
        main.freezer.run(port=5000, debug=True)
    else:
        main.freezer.freeze()

