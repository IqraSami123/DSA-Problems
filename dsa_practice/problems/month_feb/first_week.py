#  __________________first day 2_2_2026_____________________
def swap_values():
    """Swap two variables without using a temporary variable.
    Uses arithmetic operations (addition and subtraction) to exchange values.
    """
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(f"Before swapping the values are a = {a} and b = {b}")

    # Step 1: a becomes sum of both values
    a = a + b
    # Step 2: b becomes original value of a (a - original b = original a)
    b = a - b
    # Step 3: a becomes original value of b (a - new b = original b)
    a = a - b

    print(f"After swapping the values are a = {a} and b = {b}\n")


def check_number_sign():
    """Determine whether a number is positive, negative, or zero."""
    num = int(input("Enter your number here: "))
    
    # Check for zero first, then positive, then negative
    if num == 0:
        print("Your number is 0")
    elif num > 0:
        print("Your number is positive")
    else:
        print("Your number is negative")
    print("\n")


def simple_calculator():
    """Perform basic arithmetic operations on two numbers.
    Operations: addition, subtraction, multiplication, integer division.
    """
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    
    # Perform and display all basic arithmetic operations
    print("Sum of the values is:", a + b)
    print("Difference of the values is:", a - b)
    print("Multiplication of the values is:", a * b)
    print("Division of the values is:", a // b)  # Integer division
    print("\n")


def day1_main():
    """Run all Day 1 exercises."""
    swap_values()
    check_number_sign()
    simple_calculator()


#  __________________second day 3_2_2026_____________________
def remove_duplicate(lst) -> list:
    """Remove duplicates from a list and return sorted unique values.
    Uses set() to eliminate duplicates, then sorted() to order them.
    """
    return sorted(set(lst))
    # Note: The print below is unreachable (after return statement)


def count_frequency(lst) -> dict:
    """Count the frequency of each element in a list.
    Returns a dictionary with elements as keys and their counts as values.
    """
    freq = {}
    for item in lst:
        # If item already exists, increment its count; otherwise, initialize to 1
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
    # Note: The print below is unreachable (after return statement)


def get_value(d, *keys):
    """Safely retrieve a nested value from a dictionary.
    Accepts variable number of keys to traverse nested dictionaries.
    Returns None if any key is not found.
    """
    # Traverse the dictionary using each key in sequence
    for k in keys:
        d = d.get(k)
        if d is None:
            return None
    return d
    # Note: The print below is unreachable (after return statement)


def day2_main():
    """Run all Day 2 exercises: list operations and nested dictionary access."""
    data = {"user": {"profile": {"name": "Ali"}}}

    # Test removing duplicates from a list
    result = remove_duplicate([3, 1, 2, 3, 2, 1])
    print("Unique list:", result)
    print("\n")

    # Test counting element frequencies
    result = count_frequency([3, 1, 2, 3, 2, 1])
    print("Frequency count:", result)
    print("\n")

    # Test accessing nested dictionary values safely
    name = get_value(data, "user", "profile", "name")
    print("Nested value:", name)
    print("\n")


#  __________________third day 4_2_2026_____________________
class AreaCalculator:
    """Calculator class for computing areas of different shapes."""
    
    def area_of_circle(self):
        """Calculate the area of a circle using formula: π * r²"""
        radius = float(input("Enter the radius of the circle: "))
        return 3.14159 * radius * radius

    def area_of_rectangle(self):
        """Calculate the area of a rectangle using formula: width * height"""
        height = float(input("Enter the height of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return width * height

    def area_of_triangle(self):
        """Calculate the area of a triangle using formula: 0.5 * base * height"""
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return 0.5 * base * height

    def check_divisibility(self):
        """Check if a number is divisible by 3, 5, or both."""
        n = int(input("Enter the number:"))
        
        # Check divisibility: order matters (check both first)
        if n % 3 == 0 and n % 5 == 0:
            return f"{n} is divisible by both 3 and 5"
        elif n % 3 == 0:
            return f"{n} is divisible by 3"
        elif n % 5 == 0:
            return f"{n} is divisible by 5"
        else:
            return f"{n} is not divisible by 3 or 5"

    def find_max_value(self):
        """Find the maximum value among three numbers.
        BUG: Uses bitwise & instead of logical 'and' operator.
        """
        a = int(input("Enter the first value here:"))
        b = int(input("Enter the second value here:"))
        c = int(input("Enter the third valur here:"))  # Typo: "valur" should be "value"
        
        # BUG: Should use 'and' instead of '&' (bitwise operator)
        # Correct: if a >= b and a >= c:
        if a >= b & a >= c:
            return a
        if b >= a & b >= c:
            return b
        else:
            return c


def day3_main():
    """Run all Day 3 exercises: area calculations and number operations."""
    calculator = AreaCalculator()

    # Test circle area calculation
    result = calculator.area_of_circle()
    print("Area of Circle:", result)
    print("\n")

    # Test rectangle area calculation
    result = calculator.area_of_rectangle()
    print("Area of Rectangle:", result)
    print("\n")

    # Test triangle area calculation
    result = calculator.area_of_triangle()
    print("Area of Triangle:", result)
    print("\n")

    # Test divisibility check
    result = calculator.check_divisibility()
    print(result)
    print("\n")

    # Test finding maximum value
    result = calculator.find_max_value()
    print("Maximum value is:", result)
    print("\n")


#  __________________forth day 5_2_2026_____________________  # Typo: "forth" should be "fourth"
class Day4:
    """Collection of Day 4 exercises: string/number manipulation."""
    
    def romman_to_int(self, s):
        """Convert Roman numerals to integer.
        Uses subtraction rule: if a smaller numeral appears before a larger one,
        it's subtracted (e.g., IV = 4, IX = 9).
        """
        # Mapping of Roman numerals to their integer values
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0

        for i in range(len(s)):
            # If current value is less than next value, subtract it (e.g., IV, IX)
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total

    def find_grades(self, nums):
        """Assign letter grades based on numeric score.
        BUG: Line 169 has incorrect logic (> 80 instead of < 80).
        """
        if nums >= 90:
            print("Grade is A")
        elif nums >= 80 and nums < 90:
            print("Grade is B")
        elif nums >= 70 and nums > 80:  # BUG: Should be 'nums < 80' not '> 80'
            print("Grade is C")
        elif nums >= 60 and nums < 70:
            print("Grade is D")
        elif nums >= 50 and nums < 60:
            print("Grade is E")
        else:
            return "You are Fail"

    def leap_year(self, year):
        """Check if a year is a leap year.
        BUG: Incorrect logic - checks if divisible by 2 instead of proper leap year rules.
        Correct logic: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        """
        # BUG: This checks if year is even, not if it's a leap year
        if year % 2 == 0:
            return "This is leap year"
        else:
            return "This is not leap year"

    def palandrom(self, s):  # Typo: "palandrom" should be "palindrome"
        """Check if a string is a palindrome (reads the same forwards and backwards).
        Uses Python string slicing [::-1] to reverse the string.
        """
        # Compare string with its reverse
        if s == s[::-1]:
            return "This is palandrom string"  # Typo: "palandrom" should be "palindrome"
        else:
            return "This is not palandrom string"


def day4_main():
    """Run all Day 4 exercises: Roman numerals, grades, leap year, palindrome."""
    functions = Day4()

    # Test Roman numeral conversion (MCMXCIV = 1994)
    result = functions.romman_to_int("MCMXCIV")
    print(result)
    print("\n")

    # Test grade assignment for score 45
    result = functions.find_grades(45)
    print(result)
    print("\n")

    # Test leap year check for 2012
    result = functions.leap_year(2012)
    print(result)
    print("\n")

    # Test palindrome check
    result = functions.palandrom("iqrasami")
    print(result)
    print("\n")


#  __________________fifth day 6_2_2026_____________________
class Day5:
    """Collection of Day 5 exercises: patterns and sequences."""
    
    def pattern(self):
        """Print an increasing star pattern.
        Output:
        (empty)
        *
        **
        ***
        ****
        *****
        """
        for i in range(0, 6):
            # Print i stars on each line
            for j in range(i):
                print("*", end="")
            print()  # New line after each row

    def reverse_pattern(self):
        """Print a decreasing star pattern.
        Output:
        ******
        *****
        ****
        ***
        **
        *
        """
        for i in range(6, 0, -1):
            # Print i stars on each line, decreasing from 6 to 1
            for j in range(i):
                print("*", end="")
            print()  # New line after each row

    def num_pattern(self):
        """Print an increasing number pattern.
        Output:
        1
        12
        123
        1234
        12345
        """
        for i in range(1, 6):
            # Print numbers from 1 to i on each line
            for j in range(1, i + 1):
                print(j, end="")
            print()  # New line after each row

    def rev_num_pattern(self):
        """Print a decreasing number pattern.
        Output:
        123456
        12345
        1234
        123
        12
        1
        """
        for i in range(6, 0, -1):
            # Print numbers from 1 to i on each line, decreasing rows
            for j in range(1, i + 1):
                print(j, end="")
            print()  # New line after each row

    def fibnonci_no(self):  # Typo: "fibnonci" should be "fibonacci"
        """Print the first 10 Fibonacci numbers.
        Fibonacci sequence: each number is the sum of the two preceding ones.
        Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
        """
        a = 0  # First Fibonacci number
        b = 1  # Second Fibonacci number

        for i in range(10):
            print(a, end="")
            # Calculate next Fibonacci number
            next = a + b
            a = b  # Move b to a
            b = next  # Store the new Fibonacci number

    def sum_of_n_no(self):
        """Calculate and print the sum of first n natural numbers.
        For n=10: 0+1+2+3+4+5+6+7+8+9 = 45
        """
        total = 0
        n = 10
        # Sum all numbers from 0 to n-1
        for i in range(0, n):
            total += i
        print(total)


def day5_main():
    """Run all Day 5 exercises: patterns, Fibonacci, and sum."""
    functions = Day5()

    # Print increasing star pattern
    functions.pattern()
    print("\n")

    # Print decreasing star pattern
    functions.reverse_pattern()
    print("\n ")

    # Print increasing number pattern
    functions.num_pattern()
    print("\n")

    # Print decreasing number pattern
    functions.rev_num_pattern()
    print("\n")

    # Print Fibonacci sequence
    functions.fibnonci_no()
    print("\n")

    # Print sum of first n numbers
    functions.sum_of_n_no()
    print("\n")


#  __________________run all days_____________________
def main():
    """Main entry point: runs all daily exercises sequentially."""
    print("----- Day 1 -----")
    day1_main()

    print("----- Day 2 -----")
    day2_main()

    print("----- Day 3 -----")
    day3_main()

    print("------ Day 4 ----")
    day4_main()

    print("------ Day 5 ----")
    day5_main()


if __name__ == "__main__":
    # Execute main() only when script is run directly (not imported)
    main()
