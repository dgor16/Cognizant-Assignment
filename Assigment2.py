# Ask the user for a starting number
start = int(input("Enter the starting number: "))

# Count down to 1 using a while loop
while start > 0:
    print(start, end=" ")
    start -= 1

# Celebratory message
print("Blast off!")

# Generate and print the multiplication table from 1 to 10
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Ask the user for a number
n = int(input("Enter a number: "))

# Initialize a variable to hold the factorial result
factorial = 1

# Multiply factorial by each number from 1 to n
for i in range(1, n + 1):
    factorial *= i

# Display the result
print(f"The factorial of {n} is {factorial}.")