alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]

def search(letter):
    for c in range(len(alphabet)):
        if letter == alphabet[c]:
            return c
    return -1

def encrypted(text, shift, direction):
    result = []
    alphabet_size = len(alphabet)

    for i in range(len(text)):
        pos = search(text[i])
        if pos == -1:
            # Caracter no alfabético, se deja igual
            result.append(text[i])
            print(f"Letter {i} ('{text[i]}') is not in alphabet, kept as is")
            continue
        
        if direction == "encode":
            new_pos = (pos + shift) % alphabet_size
            result.append(alphabet[new_pos])
            print(f"Letter {i} encoded is {alphabet[new_pos]}")
        elif direction == "decode":
            new_pos = (pos - shift) % alphabet_size
            result.append(alphabet[new_pos])
            print(f"Letter {i} decoded is {alphabet[new_pos]}")
    return "".join(result)


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid direction. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    output = encrypted(text, shift, direction)
    print(f"\nThe {direction}d text is: {output}")

    again = input("\nDo you want to go again? Type 'yes' or 'no': \n").lower()
    if again != "yes":
        print("Goodbye!")
        break
