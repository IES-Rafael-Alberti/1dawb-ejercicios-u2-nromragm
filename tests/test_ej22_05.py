import pytest
from src.ej22_05 import capital_obtenido

@pytest.mark.parametrize(
    "input_n1, input_n2, input_n3, expected",
    [
        (1000, 10, 1, "Año 1: Capital obtenido = 1100.00€\n"),
        (10, 10, 5, "Año 1: Capital obtenido = 11.00€\nAño 2: Capital obtenido = 12.10€\nAño 3: Capital obtenido = 13.31€\nAño 4: Capital obtenido = 14.64€\nAño 5: Capital obtenido = 16.11€\n")
    ]
)

def test_capital_obtenido_params(input_n1, input_n2, input_n3, expected):
    assert capital_obtenido(input_n1, input_n2, input_n3) == expected