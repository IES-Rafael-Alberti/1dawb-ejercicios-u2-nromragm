import pytest
from src.ej2_03 import division

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (4, 2, "2.0"),
        (10, 0, "Error: No se puede dividir por cero."),
        (34, 6, str(34/6))
        
    ]
)
def test_division_params(input_n1, input_n2, expected):
    assert division(input_n1, input_n2) == expected