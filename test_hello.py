"""Regression coverage for the input boundaries raised in code review."""
from pathlib import Path
import subprocess
import sys
import unittest

from hello import greeting


class GreetingTests(unittest.TestCase):
    def test_default_name(self):
        self.assertEqual(greeting(), "Hello, World!")

    def test_named_greeting(self):
        self.assertEqual(greeting("Kirito"), "Hello, Kirito!")

    def test_trim_surrounding_whitespace(self):
        self.assertEqual(greeting("  Kirito  "), "Hello, Kirito!")

    def test_empty_name_uses_default(self):
        self.assertEqual(greeting(""), "Hello, World!")

    def test_whitespace_name_uses_default(self):
        self.assertEqual(greeting(" \t\n "), "Hello, World!")

    def test_unicode_name(self):
        self.assertEqual(greeting("世界"), "Hello, 世界!")

    def test_cli_entry_point(self):
        cases = [
            ([], "Hello, World!"),
            (["--name", "Kirito"], "Hello, Kirito!"),
            (["--name", "  Kirito  "], "Hello, Kirito!"),
            (["--name", ""], "Hello, World!"),
            (["--name", "   "], "Hello, World!"),
        ]
        script = str(Path(__file__).with_name("hello.py"))
        for arguments, expected in cases:
            with self.subTest(arguments=arguments):
                result = subprocess.run([sys.executable, script, *arguments],
                                        capture_output=True, text=True, check=False)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected + "\n")
                self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
