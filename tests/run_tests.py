"""Convenience test runner.

You can run:

    python -m tests.run_tests

or simply:

    python -m unittest
"""

from __future__ import annotations

import unittest


def main() -> None:
    loader = unittest.TestLoader()
    suite = loader.discover("tests")
    runner = unittest.TextTestRunner(verbosity=2)
    raise SystemExit(0 if runner.run(suite).wasSuccessful() else 1)


if __name__ == "__main__":
    main()
