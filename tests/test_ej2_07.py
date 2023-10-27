import pytest
from src.ej2_07 import determinar_tipo_impositivo

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (44444, "30%"),
        (99999, "45%"),
        (22222, "20%"),
        (7777, "5%"),
        (11111, "15%")
        
    ]
)
def test_determinar_tipo_impositivo_params(input_n, expected):
    assert determinar_tipo_impositivo(input_n) == expected