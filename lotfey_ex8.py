#######################################
# CS 1110A - Programming in Python    #
# Module 4 - Exercise 8 - Description #
# Author: Ahmed Lotfey                #
# Date:   04/08/2023                  #
#######################################

# calculates the sum of a series of numbers.
def series_sum(n, d):
    """calculates the sum of n terms of the series created using d as the digit.
        Args:
            n (int): number of terms.
            d (int): digit to be used in the series.
        Returns:
            int: sum of the series.
    """
    list_number = []
    for i in range(1, n + 1):
        num = i * str(d)
        list_number.append(int(num))
    return sum(list_number)


# call the function with the user input.
def main():
    # This program checks if a string is a palindrome or not.
    print("Series Sum\n")
    while True:
        try:
            n_value = int(input("Value of n: "))
        except ValueError as e:
            print(f"n must be an integer {e}")
            break
        if n_value == 0:
            print("\nDone!\n")
            break
        while True:
            try:
                d_value = int(input("Value of d: "))
            except ValueError as e:
                print(f"d must be an integer {e}")
                break
            if d_value not in range(1, 10):
                print("d must be between 1 and 9")
            else:
                break
        print(
            f"n = {n_value}   d = {d_value}   series sum = {series_sum(n_value, d_value):,}\n"
        )


# call the main function.
if __name__ == "__main__":
    main()
