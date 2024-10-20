import numpy as np
import copy

original = [0,1,2,4,5]

new_colors = np.array([
    [0, 255, 0],  # Green
    [0, 0, 255],   # Blue
    [255, 0, 0],  # Red
    [0, 0, 0],  # Black
#    [255, 255, 255]  # White
]) / 255  # Normalize to 0-1

def swap(arr, i, j):
    return_array = arr.copy()
    return_array[i], return_array[j] = arr[j], arr[i]
    return return_array

def all_permutations(arr):
    n = len(arr)
    return_array = []
    if n < 2:
        return [arr]
    elif n == 2:
        return [arr, arr[[1, 0]]]
    else:
        for i in range(n):
            sub_permutations = all_permutations(arr[:n-1])
            for perm in sub_permutations:
                return_array.append(np.vstack([perm, arr[n-1]]))
            arr[[i, n-1]] = arr[[n-1, i]]
    return return_array

import copy

def heap_permutation(array, size):
    if size == 1:
        return [np.copy(array)]
    
    permutations = []
    for i in range(size):
        # Generate permutations for size - 1
        for perm in heap_permutation(array, size - 1):
            permutations.append(np.copy(perm))

        # Swap elements back after generating permutations
        if size % 2 == 1:
            array[0], array[size - 1] = np.copy(array[size - 1]), np.copy(array[0])
        else:
            array[i], array[size - 1] = np.copy(array[size - 1]), np.copy(array[i])

    return permutations

solution = heap_permutation(new_colors, len(new_colors))
print(solution)
print(len(solution))