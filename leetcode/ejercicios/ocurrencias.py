def ocurrencias():
    lista = []
    max_reps = 0
    mas_repetido = None
    
    numero = int(input("Introduce número: "))
    while numero > 0:
        lista.append(numero)
        numero = int(input("Introduce número: "))
    
    for i in range(len(lista)):
        reps = lista.count(lista[i])
        if reps > max_reps:
            max_reps = reps
            mas_repetido = lista[i]
    
    return mas_repetido

print(ocurrencias())
