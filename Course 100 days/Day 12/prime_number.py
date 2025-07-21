numero = int(input("Pick a number"))

def is_prime(num):
    contador = 0
    isPrime = False
    for i in range(1,num):
        if num % i == 0:
            contador += 1
    if contador >= 2:
        isPrime = False
    else:
        isPrime = True
    
    return isPrime
    

print(is_prime(numero))
