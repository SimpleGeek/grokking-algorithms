import random

def quick_sort(arr):
    if len(arr) < 2:
        return arr # Base case
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([3,1,4,2,5]))