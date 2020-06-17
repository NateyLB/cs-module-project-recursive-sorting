# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB, arr, index):
    # Your code here
    # find the smaller value and insert into array at index
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            arr[index] = arrA[0]
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            arr[index] = arrB[0]
            arrB.pop(0)
        index += 1
    # get last value out of left or right
    while len(arrA) > 0:
        arr[index] = arrA[0]
        arrA.pop(0)
        index += 1
    while len(arrB) > 0:
        arr[index] = arrB[0]
        arrB.pop(0)
        index += 1
    # returns index to keep track of which one to insert to
    return index

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    #split the array down to one value per index
    if len(arr) > 1:
        split = len(arr)//2
        left = arr[:split]
        right = arr[split:]
        merge_sort(left)
        merge_sort(right)
        # create an index to keep track which index to insert to
        index = 0
        # merge
        index = merge(left, right, arr, index)
        

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

