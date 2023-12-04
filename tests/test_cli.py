"""Tests for the CLI module."""

import re
import sys

from txtstats.cli import _main


def test_main_output(tmp_path, capsys, monkeypatch, string_to_test):
    """Test the print function prints to the console."""
    # Create a temporary file with data in string_to_test
    file = tmp_path / "file_to_test.txt"
    file.write_text(string_to_test)
    # Specify a that temporary file as a command line argument
    monkeypatch.setattr(sys, "argv", [sys.argv[0], str(file)])
    # Run the function called when the txtstats console command is invoked
    _main()
    # Capture the output printed to the console by the previous command
    output = capsys.readouterr().out.rstrip()
    # Check that the command produces the expected output
    assert re.search("char_count(.*)12", output)
    assert re.search("line_count(.*)1", output)
    assert re.search("word_count(.*)2", output)
