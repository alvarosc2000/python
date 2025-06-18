# -------------------------------
# Data Types and Basic Operations
# -------------------------------

# Subscripting: accessing characters in a string
print("Subscripting example:", "Hello"[-2])  # Output: 'l'

# String concatenation
print("String concatenation:", "123" + "231")  # Output: '123231'

# Integer operations
print("Integer addition:", 123 + 23)           # Output: 146
print("Underscore for readability:", 123_332)  # Output: 123332

# Float number
print("Float example:", 32.32213)

# Boolean values
print("Boolean True:", True)
print("Boolean False:", False)

# -------------------------------
# Type Checking and Conversion
# -------------------------------

# Length of a string
print("Length of 'Hello':", len("Hello"))

# Type checking
print("Type of 'Hello':", type("Hello"))  # str
print("Type of 123:", type(123))          # int

# String to Integer conversion
print("Convert and add:", int("123") + int(7))  # Output: 130

# -------------------------------
# User Input and String Length
# -------------------------------

name_of_user = input("Enter your name: ")
len_of_name = len(name_of_user)
print("Number of letters in your name is:", len_of_name)

# -------------------------------
# Arithmetic Operations
# -------------------------------

print("Addition:", 2 + 2)
print("Subtraction:", 2 - 2)
print("Multiplication:", 2 * 2)
print("Division:", 4 / 2)
print("Integer Division:", 4 // 2)
print("Exponentiation:", 2 ** 3)

# Operator Precedence: PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)
print("PEMDAS example:", 3 * 3 + 3 / 3 - 3)  # Output: 7.0

# -------------------------------
# BMI Calculator
# -------------------------------

height = 1.65
weight = 84

# Calculate BMI
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))

# -------------------------------
# f-Strings and Mixed Data Types
# -------------------------------

score = 0
height = 1.8
is_winning = True

# Combine different data types in a formatted string
print(f"Your score is {score}, your height is {height}, and winning status is {is_winning}.")
