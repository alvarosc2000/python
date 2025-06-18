import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))


user = random.randint(1,5)
if user == 1:
    print("Alice")
elif user == 2:
    print("Bob")
elif user == 3:
    print("Charlie")
elif user == 4:
    print("David")
else:
    print("Emanuel")
