print("🍕 Welcome to Python Pizza Deliveries!")

# Initialize the price
price = 0

# Get pizza size input
size = input("What size pizza do you want? (S, M, or L): ").upper()

# Set base price based on size
if size == "S":
    price += 15
    print("Small pizza: $15")
elif size == "M":
    price += 20
    print("Medium pizza: $20")
elif size == "L":
    price += 25
    print("Large pizza: $25")
else:
    print("❌ Invalid pizza size. Please restart and choose S, M, or L.")
    exit()

# Ask for pepperoni
pepperoni = input("Do you want pepperoni? (Y or N): ").upper()
if pepperoni == "Y":
    if size == "S":
        price += 2
        print("+ Pepperoni for Small pizza: $2")
    else:
        price += 3
        print("+ Pepperoni for Medium/Large pizza: $3")

# Ask for extra cheese
extra_cheese = input("Do you want extra cheese? (Y or N): ").upper()
if extra_cheese == "Y":
    price += 1
    print("+ Extra cheese: $1")

# Final total
print(f"💰 Total price: ${price}")
