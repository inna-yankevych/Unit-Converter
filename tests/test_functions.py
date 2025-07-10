
from src.functions import convert_weight, convert_volume


def test_weight_converter():
    assert convert_weight(5000, "gram", "kilogram") == 5

def test_volume_converter():
    assert convert_volume(5, "fluid ounce", "milliliter") == 142.07
