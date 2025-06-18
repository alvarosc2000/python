print("Welcome to the rollercoaster!")
height = int(input("Whats your height in cm? "))
bill = 0

if(height >= 120):
    print("You can ride the rollercoaster")
    age = int(input("Age? "))
    if age < 10:
        bill = 10
        print("Pay 10$")
    elif age <= 18:
        bill = 18
        print("Pay 20$")
    else:
        bill = 22
        print("Pay 22$")
    
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill +=3
        print(f"Your bill is: {bill}")

else:
    print("You CANT ride the rollercoaster")



number = int(input("Number you want to check "))

if(number %2 == 0):
    print("EVEN")
else:
    print("ODD")


weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")