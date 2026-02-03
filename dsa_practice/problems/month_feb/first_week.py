

#  __________________first day 2_2_2026_____________________
# swape the values of two variables without any tenmporary variable

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(f"Before swapping the valus are a = {a} and b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping the valus are a = {a} and b = {b}")

# Check if a number is positive, negative, or zero

num = int(input("enter your number here: "))

if num == 0:
    print("Your number is 0")
elif num >= 1:
    print("Your number is positive")
elif num < 1:
    print("Your number is negative")


# Simple calculator: add, subtract, multiply, divide
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("sum of the values are:", a + b)
print("Subtract of the values are:", a - b)
print("Multiply of the values are:", a * b)
print("Division of the values are:", a // b)


#  __________________first day 2_2_2026_____________________
