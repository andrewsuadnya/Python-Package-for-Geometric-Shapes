from src.shapes.circle import calculate_area, calculate_circumference
import math


def test_calculate_area():
    assert math.isclose(calculate_area(5), 78.54, abs_tol=0.01)


def test_calculate_circumference():
    assert math.isclose(calculate_circumference(5), 31.42, abs_tol=0.01)
