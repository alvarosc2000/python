import random

word_list = ["aardvark", "baboon", "camel"]
lives = 2

# Elegir palabra al azar
chosen_word = random.choice(word_list)
print(f"Chosen word (for debugging): {chosen_word}")  # Puedes comentar esta línea en el juego real

# Crear placeholder con guiones bajos
placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over and lives > 0:
    guess = input("Introduce una letra: ").lower()

    # Si ya adivinaste esta letra antes, avisa y continúa
    if guess in correct_letters:
        print(f"Ya has adivinado la letra '{guess}'. Intenta otra.")
        continue

    display = ""
    # Actualizar display y verificar si la letra está en la palabra
    for letter in chosen_word:
        if letter == guess:
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Si el guess no está en la palabra, restar vida
    if guess not in chosen_word:
        lives -= 1
        print(f"Letra incorrecta. Te quedan {lives} vidas.")
    else:
        # Añadir letra correcta a la lista
        correct_letters.append(guess)

    print(display)

    # Verificar si ganaste
    if "_" not in display:
        game_over = True
        print("You win!")

if lives == 0:
    print(f"Game over! The word was '{chosen_word}'.")
