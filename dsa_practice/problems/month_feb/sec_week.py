#  __________________first day 24_2_2026_____________________
class Day1:
    def reverse_string(self, name):
        return name[::-1]

    def Check_palindrome(self, a):
        return a == a[::-1]

    def vowels(self, s):
        count = 0
        vowels = "aeiou"
        for i in s:
            if i in vowels:
                count += 1
        return count

    def max_list(self, list):
        maximum = list[0]

        for n in list:
            if n > maximum:
                maximum = n
        return maximum

def day1_main():

    functions = Day1()

    result = functions.reverse_string("iqra sami")
    print(result)
    print("\n")

    result = functions.Check_palindrome("iqra")
    print(result)
    print("\n")

    result = functions.vowels("iqra")
    print(result)
    print("\n")

    result = functions.max_list([4,5,6,6,7,8,2,9])
    print(result)
    print("\n")


#  __________________run all days_____________________
def main():
    """Main entry point: runs all daily exercises sequentially."""
    print("----- Day 1 -----")
    day1_main()


if __name__ == "__main__":
    # Execute main() only when script is run directly (not imported)
    main()
