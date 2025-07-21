cadena = str(input("Introduce cadena a invertir: "))

def inv(cadena):
    new_cadena = ""
    # Start stop step
    for i in range(len(cadena)-1,-1,-1):
        new_cadena += cadena[i]
    
    return new_cadena


print(inv(cadena))