def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# [span_10](start_span)Data from Lab Manual[span_10](end_span)
original_list = [9, 5, 1, 4, 3]
sorted_list = insertion_sort(original_list.copy())

print(f"Original List: {original_list}")
print(f"Sorted List: {sorted_list}")