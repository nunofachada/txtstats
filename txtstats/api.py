from typing import Any

from .stats_finder import _find_stats


def text_stats(txt: str) -> dict[str, Any]:
    """Generate statistics for the specified text.

    Args:
      s:
        The text from which to generate statistics.

    Returns:
      A dictionary containing the generated text statistics.
    """

    return {name: stat_func(txt) for name, stat_func in _find_stats().items()}
    # return {stat_func.__name__[1:]: stat_func(txt) for stat_func in _stats}
