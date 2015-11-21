# -*- coding: ISO-8859-1 -*-

"""This module displays 'Hello world !'"""

import colorise

def set_color(color):
    colorise.set_color(color)

def hello_world(color=False):

    if color:
        set_color('purple')

    print 'Hello World !'
