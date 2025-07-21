import random
import my_module

random_integer = random.randint(1,10)
print(random_integer)

# print(my_module.my_favorurite_number)

random_float_0_to_1 = random.random() * 10
print(random_float_0_to_1)

random_float= random.uniform(1,10)
print(random_float)


random_head_tails = random.randint(0,1)
if random_head_tails == 0:
    print("Heads")
else:
    print("Tails")