def insertion_sort(arr):
    # Iterate through the list starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted
        j = i-1       # Index of the last element in the sorted portion
        # Shift elements in the sorted portion that are greater than the key
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        # Insert the key into its correct position
        arr[j + 1] = key
    return arr

# Example usage:
arr = [5, 3, 4, 1]
print(insertion_sort(arr))  # Output: [1, 3, 4, 5]
