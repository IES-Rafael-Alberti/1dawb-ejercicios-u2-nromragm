import pytest
from src.ej2_09 import comprobar_edad

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (4, "La entrada vale 5€"),
        (2, "Puede entrar gratis"),
        (25, "La entrada vale 10€")
    ]
)
def test_comprobar_edad_params(input_n, expected):
    assert comprobar_edad(input_n) == expected