"""
Functions for to be invoked as command line scripts.
"""

import sys
from inspect import getdoc


def main():
    if len(sys.argv) > 1:
        from .api import text_stats

        f = sys.argv[1]
        with open(f, "r") as text_file:
            s_stats = text_stats(text_file.read())
        for stat_name in s_stats:
            print(f"\t{stat_name} : {s_stats[stat_name]}")
    else:
        from .stats_finder import _find_stats

        stats_found = _find_stats()
        for stat_name in stats_found:
            print(stat_name, "-", getdoc(stats_found[stat_name]).split("\n")[0])
