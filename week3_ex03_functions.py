#question 1

#Define a function called 'greet' that prints "Hello, World!"
def greet():
  print("Hello, World! ")

#Call the 'greet' function
greet()

#------------------------------------------------------------------------------------
#question 2

#Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
def personalized_greeting(name):
    print("Hello,",name + "!")

#Call the 'personalized_greeting' function with your name
personalized_greeting("Charlton")

#------------------------------------------------------------------------------------
#question 3

#Define a function called 'square' that takes a number as a parameter and returns its square
def square(number):
    return number * number

#Define a function called 'square' that takes a number as a parameter and returns its square
print(square(5))

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area(length, width):
    return length * width

#Call the 'rectangle_area' function with length 4 and width 5, and print the result
print(rectangle_area(4, 5))


#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(func, number):
    return func(number)

# Define a function called 'double' that takes a number as a parameter and returns its double
def double(number):
    return number * 2

# Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
print(apply_operation(double, 7))

# Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
print(apply_operation(square, 3))