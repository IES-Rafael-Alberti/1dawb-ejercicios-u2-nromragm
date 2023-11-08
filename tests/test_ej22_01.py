import pytest
from src.ej22_01 import palabra_10_veces

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("a", "a\na\na\na\na\na\na\na\na\na\n"),
        ("hola", "hola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\n")
    ]
)
def test_palabra_10_veces_params(input_n, expected):
    assert palabra_10_veces(input_n) == expected