from src.shapes.rectangle import calculate_area, calculate_perimeter


def test_calculate_area():
    assert calculate_area(4, 6) == 24


def test_calculate_perimeter():
    assert calculate_perimeter(4, 6) == 20
