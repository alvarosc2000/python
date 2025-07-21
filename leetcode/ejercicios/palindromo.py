cadena = str(input("Introduce cadena: "))

def es_palindromo(cadena):
    for i in range (0, len(cadena)//2):
        if cadena[i] != cadena[-(i+1)]:
            return False
    return True


print(es_palindromo(cadena))
