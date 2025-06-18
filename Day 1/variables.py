# Ejemplo básico de strings y prints
string = "Hello world"
print(string)

# Saltos de línea y concatenación de strings
print("First line \nSecond line")
print("Hello" + " " + "User")

# Uso de input para saludar al usuario
name = input("What is your name? ")
print("Hello " + name)

# Mostrar la longitud del nombre ingresado
print("Tu nombre tiene", len(name), "letras.")

# Receta paso a paso para hacer pan
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# Ejemplo de intercambio de valores entre variables
glass1 = "milk"
glass2 = "juice"

# Intercambiar los contenidos de glass1 y glass2 usando una variable auxiliar
aux = glass1
glass1 = glass2
glass2 = aux

print("glass1:", glass1)  # Debería imprimir 'juice'
print("glass2:", glass2)  # Debería imprimir 'milk'
