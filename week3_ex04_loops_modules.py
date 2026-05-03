# Question 1: Using a for loop with a list

#Create a list of fruits
fruits = ("pear cherry strawberry orange")

#Use a for loop to print each fruit in the list
for fruits in list("pear cherry strawberry orange"): 
  print(fruits)


#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

#Use a while loop to create a countdown from 5 to 1
count = 5

while count >=1:
  print(count)
  
  count-=1   

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

for i in range(1, 11):
    print(i ** 2)

#-------------------------------------------------------------------------
# Question 4: Using the random module

#Import the random module
import random

#Create a list of colors
colors = ("pink", "lilac", "blue", "red", "white", "black", "yellow")

#Use a for loop to select and print 3 random colors from the list
for i in range(3):
    print(random.choice(colors))

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

#Import the custom module and use its functions
import math_operations

print(math_operations.add(20, 3))
print(math_operations.subtract(65, 4))

#-------------------------------------------------------------------------
