from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4, decorator_5
import random
import cmath
import math

@decorator_4
def find_palindroms(texts):
    """
    Finds the palindromes in a give list of strings
    :param texts: a list of strings.
    """
    return list(filter(lambda x: (x == "".join(reversed(x))), texts))


@decorator_4
def sort_tuples(tuples):
    """
    Sorts a list of tuples by the second item
    :param tuples: a list of tuples that needs to be sorted 
    """
    return sorted(tuples, key=lambda x: x[1])


@decorator_4
def qudratic_solver(a, b, c):
    """
    quadratic equation solver function
    :param a: The first coefficient
    :param b: The second coefficient
    :param c: The third coefficient
    """
    d = b ** 2 - 4 * a * c  # discriminant
    sol_1 = (-b - cmath.sqrt(d)) / (2 * a)  # The first root
    sol_2 = (-b + cmath.sqrt(d)) / (2 * a)  # The second root

    print(f"The solutions are {sol_1} and {sol_2}")


@decorator_4
def pascal_triagle(num_rows):
    """
    pascal triangle printer function
    :param num_rows: The number of rows in the desired pscal triangle
    """
    for i in range(num_rows):
        print(" " * (num_rows-i), end="")

        for j in range(i+1):
            print(math.comb(i, j), end=" ")

        print()


if __name__ == "__main__":
    
    ###################################
    #      Testing the decorators     #
    ###################################
    find_palindroms(['abc', 'ava', 'b'])
    sort_tuples([('abc', 121),('abc', 231),('abc', 148), ('abc',221)])
    pascal_triagle(5)
    qudratic_solver(1, 1, 1)
    decorator_4.rank_speed()
