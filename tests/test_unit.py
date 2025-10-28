import pytest
from src.calculadora import sumar, restar, dividir, promedio

def test_sumar():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(5, 2) == 3

def test_dividir_normal():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)

def test_promedio_lista():
    assert promedio([1, 2, 3, 4]) == 2.5

def test_promedio_lista_vacia():
    with pytest.raises(ValueError):
        promedio([])
