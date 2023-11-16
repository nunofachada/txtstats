from typing import Any

def text_stats(txt: str) -> dict[str, Any]:

    wc = len(txt.split())
    lc = len(txt.split("\n"))
    cc = len(txt)

    return { "word_count": wc, "line_count": lc, "char_count": cc }

print(text_stats("Hello world\nBye world"))