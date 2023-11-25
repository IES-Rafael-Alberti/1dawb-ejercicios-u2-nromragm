import pytest
from src.ej2_04 import par_o_impar

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (4, "El numero es par"),
        (11, "El numero es impar"),
        (0, "El numero es par")
        
    ]
)
def test_par_o_impar_params(input_n, expected):
    assert par_o_impar(input_n) == expected