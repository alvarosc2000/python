# Diccionario con términos de programación
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something repeatedly."
}

# Imprimir el valor asociado a la clave "Bug"
print(programming_dictionary["Bug"])

# Crear e imprimir un diccionario vacío
empty_dictionary = {}
print(empty_dictionary)

# Editar el valor de una clave existente
programming_dictionary["Bug"] = "A mistake in the code that causes unexpected behavior."
print(programming_dictionary)

# Recorrer un diccionario e imprimir sus valores
for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")

# Add
programming_dictionary["c"]="hola"
empty_dictionary = programming_dictionary
for key in empty_dictionary:
    print(f"{key}: {empty_dictionary[key]}")