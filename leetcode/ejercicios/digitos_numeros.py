def is_letra(caracter):
    return caracter.isalpha()

def is_digit(caracter):
    return caracter.isdigit()

def contador_dig_num_ex():
    cadena = input("Introduce una cadena... ")

    contador_dig = 0
    contador_car = 0
    contador_ex = 0

    for c in cadena:
        if is_letra(c):
            contador_car += 1
        elif is_digit(c):
            contador_dig += 1
        else:
            contador_ex += 1

    print("Contador de letras:", contador_car)
    print("Contador de dígitos:", contador_dig)
    print("Contador de otros caracteres:", contador_ex)

contador_dig_num_ex()
