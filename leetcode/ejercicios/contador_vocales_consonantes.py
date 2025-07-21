

cadena = str(input("Introduce cadena... "))

def is_vocal(letra):
    vocales='aeiou'
    if letra not in vocales:
        return False
    return True


def contador(cadena):
    cadena = cadena.lower()
    contador_vocales = 0
    contador_consonantes = 0

    for i in range(0, len(cadena)):
        if cadena[i].isalpha() and is_vocal(cadena[i]):
             contador_vocales +=1
        elif cadena[i].isalpha() and not is_vocal(cadena[i]):
            contador_consonantes +=1
    
    print("Contador de vocales --> " , contador_vocales)
    print("Contador de consonantes --> ", contador_consonantes)


print(contador(cadena))