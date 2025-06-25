# functions.py

# 1. Una función simple que imprime un saludo
def my_function():
    print("Hello")
    print("Bye")


# 2. Función con un parámetro
def greet(name):
    print(f"Hello, {name}!")


# 3. Función que devuelve un valor
def add(a, b):
    return a + b


# 4. Función con una condición
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# 5. Ejecutar funciones si se ejecuta directamente el archivo
if __name__ == "__main__":
    my_function()
    greet("Alice")
    print("3 + 4 =", add(3, 4))
    print("Is 10 even?", is_even(10))
