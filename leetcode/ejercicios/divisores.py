numero = int(input("Introduce numero... "))

def divisores(numero):
    lista = []
    for i in range(1,numero+1):
        if numero % i == 0:
            lista.append(i)
    
    return lista

print(divisores(numero))