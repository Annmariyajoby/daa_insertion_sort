def insertion_sort(arr):
    # Loop from the second element up to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Place the key at its correct position
        arr[j + 1] = key
    return arr

# Example Usage
numbers = [7, 3, 9, 1, 5, 8, 2]
print("Original:", numbers)
sorted_numbers = insertion_sort(numbers)
print("Sorted:  ", sorted_numbers)