def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# [span_3](start_span)Data from Lab Manual[span_3](end_span)
original_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(original_list.copy())

print(f"Original List: {original_list}")
print(f"Sorted List: {sorted_list}")