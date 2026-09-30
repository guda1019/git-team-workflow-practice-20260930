# Git Team Workflow Demo

A tiny Python project for practicing shared-repository collaboration on GitHub.

## Run

Python 3.9 or newer; no third-party dependencies.

```sh
python3 hello.py
python3 hello.py --name Kirito
```

Expected output: `Hello, World!` and `Hello, Kirito!`, respectively.

Leading and trailing whitespace is removed from the name. Empty or
whitespace-only names fall back to `World`.

```sh
python3 hello.py --name '  Kirito  '
python3 hello.py --name '   '
```

These print `Hello, Kirito!` and `Hello, World!`, respectively.

## Verify

```sh
python3 -m unittest -v
```

The tests cover default names, ordinary names, surrounding whitespace, empty
names, whitespace-only names, Unicode names, and the command-line entry point.

## Workflow

Create a feature branch from `main`, open a pull request, request a review,
address the feedback in the same branch, and merge after approval.
