import random

# Datos simulados de cuentas/personas famosas
data = [
    {"name": "Instagram", "followers": 600, "description": "Social media platform"},
    {"name": "Cristiano Ronaldo", "followers": 570, "description": "Footballer"},
    {"name": "Ariana Grande", "followers": 380, "description": "Singer and actress"},
    {"name": "Dwayne Johnson", "followers": 390, "description": "Actor and wrestler"},
    {"name": "Kylie Jenner", "followers": 420, "description": "Reality TV star and businesswoman"},
    {"name": "Lionel Messi", "followers": 470, "description": "Footballer"},
    {"name": "Selena Gomez", "followers": 430, "description": "Singer and actress"},
    {"name": "Taylor Swift", "followers": 410, "description": "Singer-songwriter"},
]

def get_random_account():
    """Selecciona una cuenta aleatoria del dataset."""
    return random.choice(data)

def format_account(account):
    """Formatea la información de una cuenta para mostrarla al usuario."""
    name = account["name"]
    description = account["description"]
    return f"{name}, a {description}"

def check_answer(guess, a_followers, b_followers):
    """Devuelve True si el usuario adivinó correctamente, False en caso contrario."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        while account_a == account_b:
            account_b = get_random_account()

        print(f"\nCompare A: {format_account(account_a)}")
        print("vs")
        print(f"Compare B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers = account_a["followers"]
        b_followers = account_b["followers"]

        is_correct = check_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            account_a = account_b
            account_b = get_random_account()
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Ejecutar el juego
game()
