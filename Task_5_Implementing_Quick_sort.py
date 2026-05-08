def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Using the middle element as the pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Dataset from Task 5
data = [10, 7, 8, 9, 1, 5]
print(f"Original List: {data}")
print(f"Sorted List: {quick_sort(data)}")