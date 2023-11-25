import pytest
from src.ej2_02 import validar_password

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("sapo", False),
        ("contraseña", True),
        ("CONTRASEÑA", True),
        ("Hola", False),
        ("CoNtRaSeÑa", True),
        (str(4), False),
        ("4", False)
        
    ]
)
def test_password_params(input_n, expected):
    assert validar_password(input_n) == expected