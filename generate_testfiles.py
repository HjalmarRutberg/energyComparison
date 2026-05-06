"""Generates test files with random integers for testing the merge sort 
implementation. Do not delete existing files!"""
import errno
import os
import random

FLAGS = os.O_CREAT | os.O_EXCL | os.O_WRONLY

def generate_test_file(filename, num_elements):
    """Generates a test file with random integers."""
    try:
        os.open(filename, FLAGS)
    except OSError as e:
        if e.errno == errno.EEXIST:  # Failed as the file already exists.
            print(f"File '{filename}' already exists. Skipping generation.")
            return
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(num_elements):
            f.write(f"{random.randint(0, 1000000)}\n")

generate_test_file('test_inputs/test_input_1000.txt', 1000)
generate_test_file('test_inputs/test_input_100000.txt', 100000)
generate_test_file('test_inputs/test_input_10000000.txt', 10000000)
