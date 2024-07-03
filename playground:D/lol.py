def quicksort(arr, low, high, pivot_index):
    if low < high:
        # Partition the array and get the index of the pivot element
        pivot_index = partition(arr, low, high, pivot_index)

        # Recursively sort the subarrays on either side of the pivot
        quicksort(arr, low, pivot_index - 1, pivot_index)
        quicksort(arr, pivot_index + 1, high, pivot_index)

def partition(arr, low, high, pivot_index):
    # Move the pivot element to the end
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    pivot = arr[high]

    # Indices for elements less than the pivot
    i = low - 1

    # Traverse the array and rearrange elements
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print("Swapping:", arr[i], "and", arr[j])

    # Move the pivot element to its final position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print("Swapping (pivot):", arr[i + 1], "and", arr[high])

    return i + 1

# Example usage:
arr = [6, 2, 9, 7, 3, 10, 5]
custom_pivot_index = 3  # Choose a custom pivot index (0-based)

print("Original array:", arr)
quicksort(arr, 0, len(arr) - 1, custom_pivot_index)
print("Sorted array:", arr)
