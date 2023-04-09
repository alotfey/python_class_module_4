################################################
# CS 1110A - Programming in Python             #
# Module 4 - Program 4 - Categorize Triangles  #
# Author: Ahmed Lotfey                         #
# Date:   04/10/2023                           #
################################################


def kind(a, b, c):
    """Check if triangle can be created with those lengths for sides."""
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid value cannot be negative or zero"
    elif a + b <= c or b + c <= a or a + c <= b:
        return 0
    elif a == b and b == c:
        return 1
    elif a == b or b == c or a == c:
        return 2
    elif (
        a**2 + b**2 == c**2
        or b**2 + c**2 == a**2
        or a**2 + c**2 == b**2
    ):
        return 3
    elif a * a + b * b > c * c and b * b + c * c > a * a and a * a + c * c > b * b:
        return 4
    else:
        return 5


def name(k):
    """print the triangle type."""
    triangle = kind(k[0], k[1], k[2])
    if triangle == 0:
        print(
            "{:>2},{:>3},{:>3}{:>6}{:>4}no triangle".format(
                k[0], k[1], k[2], triangle, ""
            )
        )
    elif triangle == 1:
        print(
            "{:>2},{:>3},{:>3}{:>6}{:>4}equilateral".format(
                k[0], k[1], k[2], triangle, ""
            )
        )
    elif triangle == 2:
        print(
            "{:>2},{:>3},{:>3}{:>6}{:>4}isosceles".format(
                k[0], k[1], k[2], triangle, ""
            )
        )
    elif triangle == 3:
        print("{:>2},{:>3},{:>3}{:>6}{:>4}right".format(k[0], k[1], k[2], triangle, ""))
    elif triangle == 4:
        print("{:>2},{:>3},{:>3}{:>6}{:>4}acute".format(k[0], k[1], k[2], triangle, ""))
    elif triangle == 5:
        print(
            "{:>2},{:>3},{:>3}{:>6}{:>4}obtuse".format(k[0], k[1], k[2], triangle, "")
        )


# call the function with the user input.
def main():
    # This program checks if a string is a palindrome or not.
    print("Categorize Triangles\n")
    print("  Sides      Kind   Triangle Name")
    print(" ---------   ----   -------------")
    name([1, 2, 33])
    name([5, 5, 5])
    name([6, 6, 4])
    name([3, 4, 5])
    name([7, 8, 9])
    name([4, 5, 8])

    print()
    while True:
        first_side = int(input("First side:{:<4}".format("")))
        if first_side == 0:
            print("\nDone!\n")
            break
        second_side = int(input("Second side:{:<3}".format("")))
        third_side = int(input("Third side:{:<4}".format("")))

        # tringle side list
        tringle_side_list = [first_side, second_side, third_side]
        name(tringle_side_list)
        print()


# call the main function.
if __name__ == "__main__":
    main()
