# Step 1: Ask for the user's age
age = int(input("How old are you? "))  # Convert the input into an integer

# Step 2: Check if the user is eligible to vote
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    years_left = 18 - age  # Calculate how many years are left
    print(f"Oops! You’re not eligible yet. But hey, only {years_left} more year{'s' if years_left > 1 else ''} to go!")