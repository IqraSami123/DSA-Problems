#  __________________first day 2_2_2026_____________________
def swap_values():
    # Swap the values of two variables without any temporary variable
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(f"Before swapping the values are a = {a} and b = {b}")

    a = a + b
    b = a - b
    a = a - b

    print(f"After swapping the values are a = {a} and b = {b}\n")


def check_number_sign():
    # Check if a number is positive, negative, or zero
    num = int(input("Enter your number here: "))
    if num == 0:
        print("Your number is 0")
    elif num > 0:
        print("Your number is positive")
    else:
        print("Your number is negative")
    print("\n")


def simple_calculator():
    # Simple calculator: add, subtract, multiply, divide
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print("Sum of the values is:", a + b)
    print("Difference of the values is:", a - b)
    print("Multiplication of the values is:", a * b)
    print("Division of the values is:", a // b)
    print("\n")


def day1_main():
    swap_values()
    check_number_sign()
    simple_calculator()


#  __________________second day 3_2_2026_____________________
def remove_duplicate(lst) -> list:
    return sorted(set(lst))
    print("\n")


def count_frequency(lst) -> dict:
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
    print("\n")


def get_value(d, *keys):
    for k in keys:
        d = d.get(k)
        if d is None:
            return None
    return d
    print("\n")


def day2_main():
    data = {"user": {"profile": {"name": "Ali"}}}

    result = remove_duplicate([3, 1, 2, 3, 2, 1])
    print("Unique list:", result)
    print("\n")

    result = count_frequency([3, 1, 2, 3, 2, 1])
    print("Frequency count:", result)
    print("\n")

    name = get_value(data, "user", "profile", "name")
    print("Nested value:", name)
    print("\n")


#  __________________third day 4_2_2026_____________________
class AreaCalculator:
    def area_of_circle(self):
        radius = float(input("Enter the radius of the circle: "))
        return 3.14159 * radius * radius

    def area_of_rectangle(self):
        height = float(input("Enter the height of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return width * height

    def area_of_triangle(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return 0.5 * base * height

    def check_divisibility(self):
        n = int(input("Enter the number:"))
        if n % 3 == 0 and n % 5 == 0:
            return f"{n} is divisible by both 3 and 5"
        elif n % 3 == 0:
            return f"{n} is divisible by 3"
        elif n % 5 == 0:
            return f"{n} is divisible by 5"
        else:
            return f"{n} is not divisible by 3 or 5"

    def find_max_value(self):
        a = int(input("Enter the first value here:"))
        b = int(input("Enter the second value here:"))
        c = int(input("Enter the third valur here:"))
        if a >= b & a >= c:
            return a
        if b >= a & b >= c:
            return b
        else:
            return c


def day3_main():
    calculator = AreaCalculator()

    result = calculator.area_of_circle()
    print("Area of Circle:", result)
    print("\n")

    result = calculator.area_of_rectangle()
    print("Area of Rectangle:", result)
    print("\n")

    result = calculator.area_of_triangle()
    print("Area of Triangle:", result)
    print("\n")

    result = calculator.check_divisibility()
    print(result)
    print("\n")

    result = calculator.find_max_value()
    print("Maximum value is:", result)
    print("\n")


#  __________________third day 4_2_2026_____________________
class Day4:
    def romman_to_int(self, s):
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total

    def find_grades(self, nums):
        if nums >= 90:
            print("Grade is A")
        elif nums >= 80 and nums < 90:
            print("Grade is B")
        elif nums >= 70 and nums > 80:
            print("Grade is C")
        elif nums >= 60 and nums < 70:
            print("Grade is D")
        elif nums >= 50 and nums < 60:
            print("Grade is E")
        else:
            return "You are Fail"

    def leap_year(self, year):
        if year % 2 == 0:
            return "This is leap year"
        else:
            return "This is not leap year"

    def palandrom(self, s):
        if s == s[::-1]:
            return "This is palandrom string"
        else:
            return "This is not palandrom string"


def day4_main():
    functions = Day4()

    result = functions.romman_to_int("MCMXCIV")
    print(result)
    print("\n")

    result = functions.find_grades(45)
    print(result)
    print("\n")

    result = functions.leap_year(2012)
    print(result)
    print("\n")

    result = functions.palandrom("iqrasami")
    print(result)
    print("\n")


#  __________________run all days_____________________
def main():
    print("----- Day 1 -----")
    day1_main()

    print("----- Day 2 -----")
    day2_main()

    print("----- Day 3 -----")
    day3_main()

    print("------ Day 4 ----")
    day4_main()


if __name__ == "__main__":
    main()


# no code for today
