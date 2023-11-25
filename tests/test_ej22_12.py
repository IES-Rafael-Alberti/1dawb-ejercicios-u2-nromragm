import pytest
from src.ej22_12 import veces_letra_enfrase

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("hola","a", "La letra a aparece 1 veces en la frase."),
        ("sapo","o", "La letra o aparece 1 veces en la frase."),
        ("tengo hambre", "e", "La letra e aparece 2 veces en la frase.")
    ]
)

def test_veces_letra_enfrase_params(input_n1, input_n2, expected):
    assert veces_letra_enfrase(input_n1, input_n2) == expected