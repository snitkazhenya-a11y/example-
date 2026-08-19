def is_even(number:int) -> bool:
    return (number & 1) == 0
print(is_even(2))
print(is_even(3))
print(is_even(7))


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]