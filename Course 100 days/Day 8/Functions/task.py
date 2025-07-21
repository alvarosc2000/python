def greet():
    print("greet 1")
    print("greet 2")
    print("greet 3")

greet()


def function_with_inputs(name):
    print(name)

function_with_inputs("hola mundo")


def greet_with(name, location):
    print(f"Hello {name}, your location is {location}")

name_input = input("What is your name?: ")
location_input = input("What is your location?: ")

greet_with(name_input,location_input)


#Positional arguments
greet_with(name="pepe", location="malaga")