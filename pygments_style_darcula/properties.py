# -*- coding: utf-8 -*-
"""
Darcula for .properties files
-----------------------------
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal
import base

class DarculaPropertiesStyle(Style):

    default_style = ''

    background_color = base.BACKGROUND
    highlight_color = base.SELECTION

    styles = {
        # No corresponding class for the following:
        Text:                      base.FOREGROUND, # class:  ''
        Whitespace:                "",              # class: 'w'
        Error:                     base.RED,        # class: 'err'
        Other:                     "",              # class 'x'

        Comment:                   base.GRAY,   # class: 'c'

        Operator:                  base.FOREGROUND, # class: 'o'

        Name.Attribute:            base.ORANGE, # class: 'na' - to be revised

        String:                    base.GREEN,  # class: 's'
    }