# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB, arr, index):
    # Your code here
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            arr[index] = arrA[0]
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            arr[index] = arrB[0]
            arrB.pop(0)
        index += 1

    while len(arrA) > 0:
        arr[index] = arrA[0]
        arrA.pop(0)
        index += 1
    while len(arrB) > 0:
        arr[index] = arrB[0]
        arrB.pop(0)
        index += 1

    return index

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    #split the array down to one value per index
    if len(arr) > 1:
        split = len(arr)//2
        left = arr[:split]
        right = arr[split:]
        print(left, "left")
        print(right, "right")
        merge_sort(left)
        merge_sort(right)
        index = 0
        index = merge(left, right, arr, index)
        

    return arr
test = [9,4,8,2,6,5,7,1]
print(merge_sort(test))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

