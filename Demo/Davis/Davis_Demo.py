# Lambda Demo:
xaddy = lambda x , y: x + y

print("Sum:", xaddy(20,10))

# Map Demo:
user_input = input("Enter numbers with spaces: ")

integers = list(map(int, user_input.split()))

print(f"Integers: {integers}")

# Lambda and Map Demo:
#USER INPUT NUMBERS, SPLIT THE NUMBERS AND CUBE IT USING LAMBDA AND MAP

user_input = input("Enter numbers with spaces: ")

integers = list(map(int, user_input.split()))

strIntegers = list(user_input.split())

print(f"Integers: {integers}")

cubedIntegers = list(map(lambda x: x**3, integers))

print(f"Cubed Integers: {cubedIntegers}")