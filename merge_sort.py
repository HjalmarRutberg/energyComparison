"""Merge Sort Implementation in Python"""
import sys

def load_input(input_txt):
    """Loading input from .txt file to list"""
    with open(input_txt, 'r', encoding='utf-8') as f:
        data = [int(line.strip()) for line in f]
    return data

def merge_sort(input_array, start, end):
    """Recursive merge sort function that divides the input array and 
    calls the merge function to sort and merge the divided arrays."""
    if start < end:
        mid = (start + end) // 2
        merge_sort(input_array, start, mid)
        merge_sort(input_array, mid+1, end)
        merge(input_array, start, mid, end)

def merge(input_array, start, mid, end):
    """Merging function that takes two sorted subarrays and merges them 
    into a single sorted array."""
    len1 = mid - start + 1
    len2 = end - mid
    left_arr = [0] * len1
    right_arr = [0] * len2

    for i in range(len1):
        left_arr[i] = input_array[start + i]
    for j in range(len2):
        right_arr[j] = input_array[mid + 1 + j]

    i = 0
    j = 0
    k = start

    while i < len1 and j < len2:
        if left_arr[i] <= right_arr[j]:
            input_array[k] = left_arr[i]
            i += 1
        else:
            input_array[k] = right_arr[j]
            j += 1
        k += 1

    while i < len1:
        input_array[k] = left_arr[i]
        i += 1
        k += 1

    while j < len2:
        input_array[k] = right_arr[j]
        j += 1
        k += 1

def is_sorted(input_array):
    return all(input_array[i] <= input_array[i+1] for i in range(len(input_array)-1))

if __name__ == "__main__":
    input_string = sys.argv[1]
    n_loops = int(sys.argv[2])
    array = load_input(input_string)
    unsorted_array = array.copy()
    for _ in range(n_loops):
        merge_sort(array, 0, len(array)-1)
        array = unsorted_array.copy()
    if is_sorted(input_array=array):
        print("Sort successful")
    else:
        print("Sort failed")
