"""Short program that calculates the sum of squares of a list of integers 
from a .txt file."""
import sys

def load_input(input_txt):
    """Loading input from .txt file to list"""
    with open(input_txt, 'r', encoding='utf-8') as f:
        data = [int(line.strip()) for line in f]
    return data

def sum_of_squares(input_array):
    """Returns the sum of squares of the input array."""
    return sum(x**2 for x in input_array)

if __name__ == "__main__":
    input_string = sys.argv[1]
    array = load_input(input_string)
    result = sum_of_squares(array)
    print(result)
