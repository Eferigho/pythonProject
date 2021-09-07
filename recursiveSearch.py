def recursive_binary_search(arr, target):
    if len(arr) == 0:
        return False
    else:
        midpoint = len(arr) // 2
        if arr[midpoint] == target:
            return True
        else:
            if arr[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(results):
    print("number found is:", results)

num = [1,2,3,4,5,6,7,8]
results = recursive_binary_search(num, 3)
verify(results)
