def binary_search(list, item):
    # Low and high are indices, not actual
    # values from the list
    low = 0
    high = len(list)-1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None


a_list = [1, 2, 3, 4, 5]

print(binary_search(a_list, 2))
print(binary_search(a_list, 16))