import pytest
from src.ej2_06 import determinar_grupo

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("Carlos", "H", "B"),
        ("Sapillo", "H", "A"),
        ("Maria", "M", "B"),
        ("Andrea", "M", "A")
        
    ]
)
def test_determinar_grupo_params(input_n1, input_n2, expected):
    assert determinar_grupo(input_n1, input_n2) == expected