import sys

def load_input(input_txt):
    """Loading input from .txt file to list"""
    with open(input_txt, 'r', encoding='utf-8') as f:
        data = [int(line.strip()) for line in f]
    return data

def merge_sort(input_array, start, end):
    """MergeSort"""
    if start < end:
        mid = start + (end-start)/2
        merge_sort(input_array, start, mid)
        merge_sort(input_array, mid+1, end)
        merge(input_array, start, mid, end)

def merge(input_array, start, mid, end):
    """The merge part of merge sort"""
    len1 = mid - start + 1
    len2 = end - mid
    left_arr = []
    right_arr = []

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
    return all(input_array[i] <= input_array[i+1] for i in range(len(input_array)))

if __name__ == "__main__":
    input_string = sys.argv[1]
    array = load_input(input_string)   
    merge_sort(array, 0, len(array)-1)
    if is_sorted(input_array=array):
        print("Sort successful")
    else:
        print("Sort failed")
