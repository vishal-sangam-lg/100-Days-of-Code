programming_dictionary = {
    "Bug": "An Error in in program that prevents the program from running as expected.",
    "Function": "A Piece of code that you can easily call over and over again"
}

# Retrieving items from dictionary
print(programming_dictionary["Bug"])

# Adding new item to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}
print(empty_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through dictionary
print("Looping:")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nested dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting Dictionary in a list
travel_logs = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]
