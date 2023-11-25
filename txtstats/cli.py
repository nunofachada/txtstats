"""
Functions for to be invoked as command line scripts.
"""

import sys
from inspect import getdoc
from tabulate import tabulate


def _main():
    if len(sys.argv) > 1:
        from .api import text_stats

        f = sys.argv[1]
        with open(f, "r") as text_file:
            s_stats = text_stats(text_file.read())
        print(
            tabulate(
                s_stats.items(),
                headers=["Statistic", "Value"],
                tablefmt="rounded_outline",
            )
        )

    else:
        from .stats_finder import _find_stats

        stats_found = _find_stats()

        stats_help = {k: getdoc(v).split("\n")[0] for k, v in stats_found.items()}

        print(
            tabulate(
                stats_help.items(),
                headers=["Statistic", "Description"],
                tablefmt="rounded_outline",
            )
        )
