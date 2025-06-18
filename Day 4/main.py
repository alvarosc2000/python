import random

# Opciones posibles
options = ["Rock", "Paper", "Scissors"]

# Solicitar al usuario su elección
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

# Verificar que el input sea un número válido
if user_input.isdigit():
    user_choice = int(user_input)
    if user_choice >= 0 and user_choice <= 2:
        print(f"You chose {options[user_choice]}")
        
        # Elección aleatoria de la computadora
        computer_choice = random.randint(0, 2)
        print(f"Computer chose {options[computer_choice]}\n")
        
        # Resultado
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid number. Please choose 0, 1, or 2.")
else:
    print("Invalid input. Please enter a number (0, 1, or 2).")
