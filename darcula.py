# -*- coding: utf-8 -*-
"""
Darcula
---------------------
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


BACKGROUND = "#2B2B2B"
SELECTION = "#214283"
FOREGROUND = "#A9B7C6"

COMMENT = "#808072"
ORANGE = "#CB772F"
PURPLE = "#9876AA"
YELLOW = "#F1C829"
GOLD = "#FFC66D"
EMERALD = "#88BE05"
GREEN = "#6A8759"
AQUA = "#6897BB"

class DarculaStyle(Style):

    default_style = ''

    background_color = BACKGROUND
    highlight_color = SELECTION

    styles = {
        # No corresponding class for the following:
        Text:                      FOREGROUND,  # class:  ''
        Whitespace:                "",          # class: 'w'
        Error:                     "#960050",   # class: 'err'
        Other:                     "",          # class 'x'

        Comment:                   COMMENT,   # class: 'c'
        Comment.Multiline:         "",        # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'

        Keyword:                   ORANGE,     # class: 'k'
        Keyword.Constant:          "",         # class: 'kc'
        Keyword.Declaration:       "",         # class: 'kd'
        Keyword.Namespace:         ORANGE,     # class: 'kn'
        Keyword.Pseudo:            "",         # class: 'kp'
        Keyword.Reserved:          "",         # class: 'kr'
        Keyword.Type:              "",         # class: 'kt'

        Operator:                  FOREGROUND, # class: 'o'
        Operator.Word:             "",         # class: 'ow' - like keywords

        Punctuation:               FOREGROUND,  # class: 'p'

        Name:                      FOREGROUND,  # class: 'n'
        Name.Attribute:            PURPLE,      # class: 'na' - to be revised
        Name.Builtin:              "",          # class: 'nb'
        Name.Builtin.Pseudo:       "",          # class: 'bp'
        Name.Class:                "",          # class: 'nc' - to be revised
        Name.Constant:             ORANGE,      # class: 'no' - to be revised
        Name.Decorator:            YELLOW,      # class: 'nd' - to be revised
        Name.Entity:               "",          # class: 'ni'
        Name.Exception:            EMERALD,     # class: 'ne'
        Name.Function:             GOLD,        # class: 'nf'
        Name.Property:             "",          # class: 'py'
        Name.Label:                "",          # class: 'nl'
        Name.Namespace:            "",          # class: 'nn' - to be revised
        Name.Other:                EMERALD,     # class: 'nx'
        Name.Tag:                  YELLOW,      # class: 'nt' - like a keyword
        Name.Variable:             "",          # class: 'nv' - to be revised
        Name.Variable.Class:       "",          # class: 'vc' - to be revised
        Name.Variable.Global:      "",          # class: 'vg' - to be revised
        Name.Variable.Instance:    "",          # class: 'vi' - to be revised

        Number:                    AQUA,      # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'

        Literal:                   AQUA,      # class: 'l'
        Literal.Date:              GREEN,     # class: 'ld'

        String:                    GREEN,       # class: 's'
        String.Backtick:           "",          # class: 'sb'
        String.Char:               "",          # class: 'sc'
        String.Doc:                "",          # class: 'sd' - like a comment
        String.Double:             "",          # class: 's2'
        String.Escape:             AQUA,        # class: 'se'
        String.Heredoc:            "",          # class: 'sh'
        String.Interpol:           "",          # class: 'si'
        String.Other:              "",          # class: 'sx'
        String.Regex:              "",          # class: 'sr'
        String.Single:             "",          # class: 's1'
        String.Symbol:             "",          # class: 'ss'

        Generic:                   COMMENT,               # class: 'g'
        Generic.Deleted:           FOREGROUND,            # class: 'gd',
        Generic.Emph:              "italic",              # class: 'ge'
        Generic.Error:             "",                    # class: 'gr'
        Generic.Heading:           "bold " + EMERALD,     # class: 'gh'
        Generic.Inserted:          EMERALD,               # class: 'gi'
        Generic.Output:            "",                    # class: 'go'
        Generic.Prompt:            "bold " + COMMENT,     # class: 'gp'
        Generic.Strong:            "bold",                # class: 'gs'
        Generic.Subheading:        FOREGROUND,            # class: 'gu'
        Generic.Traceback:         "",                    # class: 'gt'
    }