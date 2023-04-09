#############################################
# CS 1110A - Programming in Python          #
# Module 4 - Exercise 7 - Composite Numbers #
# Author: Ahmed Lotfey                      #
# Date:   04/08/2023                        #
#############################################


def composite(n) -> bool:
    """Yields True if n is composite and yields False if n is prime.

    Args: n (int): The number to check if it is composite or not.

    Returns: True if n is composite and False if n is prime.
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


def composite_range(a, b) -> None:
    """Yields a list of composite numbers between a and b.
    Args: a (int): The lower bound.
          b (int): The upper bound.
    """
    composite_list = []
    for i in range(a, b + 1):
        if composite(i) == True:
            composite_list.append(i)
    print(composite_list)
    print()


# call the function with the user input.
def main():
    # This program checks if a string is a palindrome or not.
    print("Composite Numbers\n")
    while True:
        ask_lower_bound = int(input("Lower bound: "))
        if ask_lower_bound == 0:
            print("\nDone!\n")
            break
        ask_upper_bound = int(input("upper bound: "))
        print(f"\nComposites in the range: {ask_lower_bound}-{ask_upper_bound}\n")
        composite_range(ask_lower_bound, ask_upper_bound)


# call the main function.
if __name__ == "__main__":
    main()
