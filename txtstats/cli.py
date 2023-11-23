"""
Functions for to be invoked as command line scripts.
"""

import sys
from inspect import getdoc

from .stats_functions import _char_count, _line_count, _word_count, text_stats


def main():
    if len(sys.argv) > 1:
        f = sys.argv[1]
        with open(f, "r") as text_file:
            s_stats = text_stats(text_file.read())
        for stat_name in s_stats:
            print(f"\t{stat_name} : {s_stats[stat_name]}")
    else:
        print(_word_count.__name__[1:], "-", getdoc(_word_count).split("\n")[0])
        print(_line_count.__name__[1:], "-", getdoc(_line_count).split("\n")[0])
        print(_char_count.__name__[1:], "-", getdoc(_char_count).split("\n")[0])
