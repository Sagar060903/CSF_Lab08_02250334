def trace_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # [span_13](start_span)Display the list after each insertion step[span_13](end_span)
        print(f"Pass {i}: {arr}")

data = [9, 5, 1, 4, 3]
trace_insertion_sort(data)