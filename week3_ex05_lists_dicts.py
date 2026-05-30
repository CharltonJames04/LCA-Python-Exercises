# Question 1: Creating and Modifying Lists

fruits = ["Lemon", "Watermelon", "Banana", "Strawberry"]
print(fruits)

# Add a fruit to the end of the list
fruits.append("Orange")

# Insert a fruit at the beginning of the list
fruits.insert(0, "Raspberry")

# Remove a fruit from the list
fruits.remove("Lemon")

# Print the modified list
print("Modified fruit list:", fruits)

#-------------------------------------------------------------------------

# Question 2: List Operations

# Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Create a new list with each number squared

squared = [num ** 2 for num in numbers]

# Find the sum and average of the original numbers
total = sum(numbers)
average = total / len(numbers)

# Print the results
print("numbers:", numbers)
print("Squared numbers:", squared)
print("Sum:", total)
print("Average:", average)

#-------------------------------------------------------------------------

# Question 3: Creating and Modifying Dictionaries

# Create a dictionary of countries and their capitals
capital = {
    "England":"London",
    "France":"Paris",
    "South Korea":"Seoul"
}
print(capital)

#Add a new country-capital pair
capital["Portugal"] = "Lisbon"

# Remove a country-capital pair
capital.pop("France")

# Print the modified dictionary
print("Modified dictionary:",capital)                                                                                                                                                                                                         #-------------------------------------------------------------------------

# Question 4: Dictionary    

# Create a dictionary of fruit colors  
fruit_colors = {
    "watermelon": "green",
    "banana": "yellow",
    "blueberry": "blue",
    "cherry": "red"
}

# Print all the fruits (keys)
print("Fruits:")
print(fruit_colors.keys())

# Print all the colors (values)
print("Colors:")
print(fruit_colors.values())

# Print each fruit and its color
print("Fruit and their colors:")

for fruit, color in fruit_colors.items():
    print(fruit, "is", color)
