# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    mid = (start + end)//2
    if start > end:
        return -1
    else:
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid-1)
        else:
            return binary_search(arr, target, mid+1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    if arr[0] < arr[len(arr)-1]:
        return binary_search(arr, target, 0, len(arr)-1)
    else:
        asc_arr = []
        for index in range(len(arr)-1, -1, -1):
            asc_arr.append(arr[index])
        reverse_index= binary_search(asc_arr, target, 0, len(asc_arr)-1)
        divisor = len(asc_arr)-1
        if reverse_index == -1:
            return -1
        else:
            return abs(reverse_index - divisor)
descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]
print(agnostic_binary_search(descending, -17))
print(agnostic_binary_search(descending, -1))


