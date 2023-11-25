import pytest
from src.ej2_05 import tributar_impuesto

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (22, 1000, "Tiene que tributar el impuesto."),
        (11, 2000, "No tiene que tributar el impuesto."),
        (35, 900, "No tiene que tributar el impuesto.")
        
    ]
)
def test_params(input_n1, input_n2, expected):
    assert tributar_impuesto(input_n1, input_n2) == expected