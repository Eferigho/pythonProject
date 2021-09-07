def binarysearch(list, target):
    left = 0
    right = len(list) - 1

    while left < right:
        midpoint = (left + right) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            right = midpoint + 1
        else:
            left = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("target has being found")
    else:
        print("Target has not being fouind")

num = [1,2,3,4,5,6,7,8,9,10]
result = binarysearch(num, 4)

verify(result)