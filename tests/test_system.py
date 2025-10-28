import subprocess

def test_cli_sumar():
    # Simula una ejecución del CLI con entrada por consola
    process = subprocess.run(
        ["python", "main.py"],
        input="1\n5\n7\n",
        text=True,
        capture_output=True
    )
    assert "Resultado: 12.0" in process.stdout
