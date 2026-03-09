# fox

## Running the (example) Python tests

This repository currently contains a small, self-contained Python service layer
under `src/services/` plus a `tests/` folder.

Run tests using the Python standard library (no extra dependencies required):

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

Or via the convenience runner:

```bash
python3 -m tests.run_tests
```