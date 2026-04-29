# Question 1: Arithmetic and Assignment Operators

#Add 3 to x using the += operator
x=55
x+=3

#Multiply y by 2 using the *= operator
y=20
y*=2

#Divide x by y and store the result in a variable called 'result
result = x / y
print(result)

#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

a=30
b=12
c=24

#Create a condition that checks if a is greater than b
a>b

#Create a condition that checks if b is even
b%2 ==0

#Create a condition that checks if c is less than or equal to a
c<=a

#Combine the above conditions using logical operators to create a 'final_condition'
(a>b)
print(a>b) 
#or
(b%2 ==0) and (c<=a)

#Print the value of 'final_condition'
print(b%2 ==0) and (c<=a)

#------------------------------------------------------------------------------------
#Question3

#Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = 82

#Implement a grading system using if-elif-else statements:
if score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
elif score >= 60:
  print("D")
else:
  print("F")

#Print the grade for the given score
print()

#------------------------------------------------------------------------------------