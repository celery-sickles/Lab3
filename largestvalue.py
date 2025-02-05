
def largest(arr):
    if not arr:
        return None
    max = arr[0]
    for i in arr:
        if (i > max):
            max = i
    return max

print(largest([1,2,3,4,5]))