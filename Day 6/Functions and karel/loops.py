# loops.py

# 1. For loop: recorrer una lista
print("For loop:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)


# 2. While loop: contar hasta 5
print("\nWhile loop:")
counter = 1
while counter <= 5:
    print("Count:", counter)
    counter += 1


# 3. Infinite loop (con break para salir)
print("\nInfinite loop example (type 'exit' to stop):")
while True:
    user_input = input("Say something (or type 'exit'): ")
    if user_input.lower() == "exit":
        print("Exiting the infinite loop.")
        break
    else:
        print("You said:", user_input)
