
from src.functions import convert_weight


def test_weight_converter():
    assert convert_weight(5000, "kilogram", "gram") == 5