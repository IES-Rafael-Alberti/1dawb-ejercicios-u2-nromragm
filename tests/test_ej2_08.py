import pytest
from src.ej2_08 import calcular_rendimiento

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (0.4, "Aceptable, 960.0€"),
        (0.8, "Meritorio, 1920.0€"),
        (0.0, "Inaceptable, 0.0€"),
        (1, "Meritorio, 2400€"),
        (0.6, "Meritorio, 1440.0€"),
        (0.3, "La puntuacion introducida no es valida.")
        
    ]
)
def test_calcular_rendimiento_params(input_n, expected):
    assert calcular_rendimiento(input_n) == expected