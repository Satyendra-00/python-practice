# Python Practice

A collection of Python exercises organized by chapter, with a small projects
folder and a `unittest` suite for selected exercises.

## Run an exercise

Run a script from the repository root. For example:

```powershell
python chapter7/p4.py
python projects/project1.py
```

Many scripts prompt for input. File handling exercises accept paths or options
on the command line; use `--help` to see the available arguments.

## Run the tests

```powershell
python -m unittest discover -s tests
```

Some early chapter files are intentionally simple demonstrations and execute
their examples when run directly.
