# - Input
name = input("What is your name? ")
print(f"Hello, {name}!")

# - Output
print("Hello, World!")
# - Variables
x = 5

# - Data Types
# Integer
x = 5

# Floating-point number
y = 3.14

# String
s = "hello"

# Boolean
b = True


# - Operators
# Addition
x = 5 + 3

# Subtraction
y = 10 - 6

# Multiplication
z = 4 * 2

# Division
a = 12 / 3

# Modulus (remainder)
b = 13 % 4


# - Decision making
x = 10

if x > 5:
	print("x is greater than 5")
else:
	print("x is not greater than 5")


# - Loops
# For loop
for i in range(5):
	print(i)

# While loop
i = 0
while i < 5:
	print(i)
	i += 1



# - Arrays
Sure! Here are code examples of each of these concepts in Python:

Input:

To get input from the user in Python, you can use the input() function:

name = input("What is your name? ")
print(f"Hello, {name}!")

This code prompts the user to enter their name, and then prints a greeting using their name.

Output:

To output text to the user in Python, you can use the print() function:

print("Hello, World!")

This code prints the string "Hello, World!" to the console.

Variables:

In Python, you can use variables to store and manipulate data. Here's an example of how to assign a value to a variable:

x = 5

This code creates a variable x and assigns it the value 5.

Data Types:

Python has several built-in data types, including integers, floating-point numbers, strings, and booleans. Here are some examples of each data type:

# Integer
x = 5

# Floating-point number
y = 3.14

# String
s = "hello"

# Boolean
b = True

Operators:

Python has several operators that you can use to perform operations on variables and data. Here are some examples:

# Addition
x = 5 + 3

# Subtraction
y = 10 - 6

# Multiplication
z = 4 * 2

# Division
a = 12 / 3

# Modulus (remainder)
b = 13 % 4

Decision making:

In Python, you can use if statements to make decisions based on the value of a condition. Here's an example:

x = 10

if x > 5:
	print("x is greater than 5")
else:
	print("x is not greater than 5")

This code checks the value of x, and prints a message depending on whether x is greater than 5.

Loops:

In Python, you can use for loops to iterate over a sequence of values, and while loops to repeat a block of code until a condition is met. Here are some examples:

# For loop
for i in range(5):
	print(i)

# While loop
i = 0
while i < 5:
	print(i)
	i += 1

The for loop in this example iterates over the values 0 through 4, and the while loop repeats the code block until i is no longer less than 5.

Arrays:

In Python, you can use lists to create arrays of values. Here's an example:

# Create an array of integers
array = [1, 2, 3, 4, 5]

# Access an element of the array
print(array[0]) # prints 1

# Modify an element of the array
array[0] = 10
print(array) # prints [10, 2, 3, 4, 5]


# - Functions
def greet(name):
	print(f"Hello, {name}!")

greet("Alice") # prints "Hello, Alice!"
greet("Bob") # prints "Hello, Bob!"
