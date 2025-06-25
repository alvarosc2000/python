capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictonary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

# Print Lille

print(travel_log["France"][1])


nested_list = ["A","2",["A", "D"]]
print(nested_list[2][1])


travel_log_nested = {
    "France":{
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany":{
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 2
    },
}

print(travel_log_nested["France"]["cities_visited"])
print(travel_log_nested["France"]["cities_visited"][2])
