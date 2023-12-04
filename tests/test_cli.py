"""Tests for the CLI module."""

import re
import sys

from txtstats.cli import _main


def test_main_output(tmp_path, capsys, monkeypatch, string_to_test):
    """Test the print function prints to the console."""
    file = tmp_path / "file_to_test.txt"
    file.write_text(string_to_test)
    monkeypatch.setattr(sys, "argv", [sys.argv[0], str(file)])
    _main()
    output = capsys.readouterr().out.rstrip()
    assert re.search("char_count(.*)12", output)
    assert re.search("line_count(.*)1", output)
    assert re.search("word_count(.*)2", output)
