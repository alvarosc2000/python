def solo_una_vez():
    my_list = []
    valor = int(input("Introduce valor (negativo para terminar): "))
    while valor >= 0:
        my_list.append(valor)
        valor = int(input("Introduce valor (negativo para terminar): "))

    my_list2 = []
    for i in range(len(my_list)):
        if my_list.count(my_list[i]) == 1:
            my_list2.append(my_list[i])
    
    print("Mostrando lista de unicos ... ")
    for i in range(len(my_list2)):
        print(my_list2[i])


print(solo_una_vez())