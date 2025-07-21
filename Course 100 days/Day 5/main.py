import random
# Lista de letras del alfabeto (minúsculas)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]

# Lista de símbolos comunes
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '=', '?', '@', '^', '_', '~']

# Lista de números del 0 al 9 como cadenas
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = []

print("Welcome to the PyPassword Generator")
n_letters = int(input("How many letters would you like in your password?: "))
n_symbols = int(input("How many symbols would you like? "))
n_numbers = int(input("How many numbers would you like? "))

for char in range (1, n_letters +1):
    random_char = random.choice(letters)
    password.append(random_char)

for char in range (1, n_symbols +1):
    random_s = random.choice(symbols)
    password.append(random_s)

for int in range (1, n_numbers +1):
    random_n= random.choice(numbers)
    password.append(random_n)


print(password)
random.shuffle(password)
print(password)


final = ""
for c in password:
    final+= c

print(f"La contraseña final es: {final}" )