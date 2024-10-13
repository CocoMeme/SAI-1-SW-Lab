docstring = '''Name: Davis Balignasay
Course/Section: BSIT-S-3A
Docstring, Lambda, and Map Function Example with User Input'''

print(docstring)

# Step 1: Get user input as a string of numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert the string input into a list of integers using map
numbers = list(map(int, user_input.split()))

# Step 3: Apply lambda and map to square each number entered by the user
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Step 4: Output the results
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
