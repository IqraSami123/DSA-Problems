

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


#  __________________second day 3_2_2026_____________________
# Remove duplicates from a list

def remove_duplicate(list) -> list:
    unique_list = sorted(set(list))
    return unique_list


# Count frequency of each element in a list

def count_frequancy(list) -> dict:
    freq = {}
    for item in list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


# Access nested dictionary values
def get_value(d, *keys):
    for k in keys:
        d = d.get(k)
        if d is None:
            return None
    return d


data = {
    "user": {
        "profile": {
            "name": "Ali"
        }
    }
}


if __name__ == "__main__":
    result = remove_duplicate([3, 1, 2, 3, 2, 1])
    print(result)
    result = count_frequancy([3, 1, 2, 3, 2, 1])
    print(result)
    name = get_value(data, "user", "profile", "name")
    print(name)


#  __________________third day 4_2_2026_____________________

