
# Describing myself using Python variables
name = "Luna"
age = 27
height = 5.6

print("Hey there, my name is", name + "!", "I’m", age, "years old and", height, "feet tall.")

# Playing with some numbers and getting fancy with math
num1 = 8
num2 = 3

# Addition
print("The sum of", num1, "and", num2, "is", num1 + num2)

# Subtraction
print("The difference when you subtract", num2, "from", num1, "is", num1 - num2)

# Multiplication
print("The product of", num1, "and", num2, "is", num1 * num2)

# Division
print("When you divide", num1, "by", num2, "you get", num1 / num2)

# Ask the user to enter a number
number = float(input("Enter a number and I’ll tell you what kind it is: "))

# Check the sign of the number
if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")