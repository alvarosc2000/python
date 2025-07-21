def ocurrencias():
    my_list = []
    valor = int(input("Introduce valor (negativo para terminar): "))
    while valor >= 0:
        my_list.append(valor)
        valor = int(input("Introduce valor (negativo para terminar): "))

    print("Ocurrencias de cada número:")
    ya_mostrados = []  # Lista para guardar qué números ya imprimimos

    for i in range(len(my_list)):
        num = my_list[i]
        if num not in ya_mostrados:
            print(num, my_list.count(num))
            ya_mostrados.append(num)  # Evitamos repetir




print(ocurrencias())
