import pytest
from src.ej22_11 import invertir_palabra

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("hola", "aloh"),
        ("sapo", "opas")
    ]
)

def test_invertir_palabra_params(input_n, expected):
    assert invertir_palabra(input_n) == expected