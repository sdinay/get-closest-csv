import pytest
from csv_parser import get_closest, distance


def test_get_closets():
    csv_file = open('tests/fixtures/example1.csv', 'r')
    assert get_closest(csv_file, 0, 4) == "Los Angeles, CA, USA"
    file.close(csv_file)

def test_same_coordinates():
    csv_file = open('tests/fixtures/example1.csv', 'r')
    assert get_closest(csv_file, 2, 3) == "chicago"
    file.close(csv_file)

def test_manhattan_distance():
    assert distance(0, 0, 1, 1) == 2

    assert distance(-1, -1, 1, 1) == 4
