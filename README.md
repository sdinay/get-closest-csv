# CSV Parser

A program that parses a CSV file containing a place, its latitude, its longitude and its type in columns 1, 2, 3 and 4 respectively using the csv module. Returns the closest place to the coordinates provided. Coordinates can be positive or negative number pairs, like ones
found on an x-y plane.

## Requirements
- python 3.6 or higher

## Setup

```
pip install --upgrade pip
pip install -r requirements.txt
```

## Run Tests

Run all tests

```
pytest
```

For a specific test

```
pytest -k test_init
```
