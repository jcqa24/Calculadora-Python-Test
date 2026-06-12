def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    if b == 0:
        return 0
    else:
        return a + multiplicacion(a, b - 2)

def division(a, b):
    if b == 0:
        return "Error: Division por cero"
    return a / b

def calculadora():
    print("Calculadora Basica")
    print("Operaciones: suma, resta, multiplicacion, division")
    print("Escribe 'salir' para terminar")

    while True:
        op = input("\nOperacion: ").lower()

        if op == "salir":
            break

        if op not in ("suma", "resta", "multiplicacion", "division"):
            print("Operacion no valida")
            continue

        try:
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
        except ValueError:
            print("Error: Ingresa numeros validos")
            continue

        if op == "suma":
            print(f"Resultado: {suma(a, b)}")
        elif op == "resta":
            print(f"Resultado: {resta(a, b)}")
        elif op == "multiplicacion":
            print(f"Resultado: {multiplicacion(a, b)}")
        elif op == "division":
            print(f"Resultado: {division(a, b)}")

if __name__ == "__main__":
    calculadora()
