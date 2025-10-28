from src.calculadora import promedio

def test_promedio_archivo():
    with open("data/numeros.txt") as f:
        numeros = [float(line.strip()) for line in f]
    resultado = promedio(numeros)
    assert resultado == 25
