print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if direction == "right":
    print("You fell into a hole. Game Over.")
elif direction == "left":
    action = input("You've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    
    if action == "swim":
        print("You were attacked by a trout. Game Over.")
    elif action == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue.\nWhich door do you choose? ").lower()
        
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Invalid action. Game Over.")
else:
    print("Invalid direction. Game Over.")
