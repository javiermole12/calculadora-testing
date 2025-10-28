from src.calculadora import sumar, restar, dividir, promedio

def main():
    print("Calculadora simple")
    print("1. Sumar\n2. Restar\n3. Dividir\n4. Promedio")
    opcion = input("Elige una opción: ")

    if opcion in ("1", "2", "3"):
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))

        if opcion == "1":
            print(f"Resultado: {sumar(a, b)}")
        elif opcion == "2":
            print(f"Resultado: {restar(a, b)}")
        elif opcion == "3":
            try:
                print(f"Resultado: {dividir(a, b)}")
            except ValueError as e:
                print(e)
    elif opcion == "4":
        valores = list(map(float, input("Introduce números separados por espacio: ").split()))
        print(f"Promedio: {promedio(valores)}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
