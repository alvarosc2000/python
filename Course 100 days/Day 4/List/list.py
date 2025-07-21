states_of_america = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
]

spanish_cities = ["Malaga" , "Sevilla", "Jaen"]

print(states_of_america[0])

states_of_america.append("España")

print(states_of_america)

states_of_america.extend(["Madrid" , "Barcelona"])
print(states_of_america)


size = (len(states_of_america))
print(states_of_america[size-1])


both = [states_of_america, spanish_cities]
print(both[1][1])