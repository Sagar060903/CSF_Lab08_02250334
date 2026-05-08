def trace_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # [span_6](start_span)Display the list after every pass[span_6](end_span)
        print(f"Pass {i+1}: {arr}")

data = [64, 34, 25, 12, 22, 11, 90]
trace_bubble_sort(data)