"""
Functions for generating text statistics.
"""

from typing import Any


def text_stats(txt: str) -> dict[str, Any]:
    """Generate statistics for the specified text.

    Args:
      s:
        The text from which to generate statistics.

    Returns:
      A dictionary containing the generated text statistics.
    """
    wc = len(txt.split())
    lc = len(txt.split("\n"))
    cc = len(txt)

    return {"word_count": wc, "line_count": lc, "char_count": cc}


if __name__ == "__main__":
    print(text_stats("Hello world\nBye world"))
