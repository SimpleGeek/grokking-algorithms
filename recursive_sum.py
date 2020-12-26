def recursive_sum(arr):
    if len(arr) < 2:
        return arr[0]
    else:
        arr[0] = arr[0] + arr[len(arr) - 1]
        arr.pop()
        return recursive_sum(arr)

print(recursive_sum([1,3,4]))