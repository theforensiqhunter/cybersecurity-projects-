# Funciones para cada operación
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error! No se puede dividir por cero."
    else:
        return x / y

# Menú principal
def menu():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

# Función principal para ejecutar el programa
def calculadora():
    while True:
        menu()

        # Obtener opción del usuario
        opcion = input("Ingresa el número de la operación que deseas realizar: ")

        # Si el usuario elige "5", salimos del programa
        if opcion == '5':
            print("¡Hasta luego!")
            break

        # Pedir los dos números
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        # Realizar la operación según la opción
        if opcion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif opcion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar la calculadora
calculadora()
