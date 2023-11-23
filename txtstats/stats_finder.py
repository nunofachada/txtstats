import sys
from typing import Any, Callable


def _find_stats() -> dict[str, Callable[[str], Any]]:
    if sys.version_info < (3, 10):
        from importlib_metadata import entry_points
    else:
        from importlib.metadata import entry_points

    discovered_plugins = entry_points(group="txtstats.stats")

    found_stats: Callable[[str], Any] = {}

    for entry_point in discovered_plugins:
        found_stats[entry_point.name] = entry_point.load()

    return found_stats
