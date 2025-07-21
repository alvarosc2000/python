def duplicados_lista():
    my_list = []
    valor = int(input("Introduce datos: "))
    while valor >= 0:
        my_list.append(valor)
        valor = int(input("Introduce datos: "))

    print("La lista tras añadir valores: ")
    for i in range(len(my_list)):
        print(my_list[i])
    
    print("Analizando si hay duplicados.... ")
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                return True

    return False

print(duplicados_lista())
