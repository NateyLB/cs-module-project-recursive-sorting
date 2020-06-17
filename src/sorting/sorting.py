# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    print(arrA, "A")
    print(arrB, "B")
    while len(arrA) > 0  and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    if len(arrA) > 0:
        merged_arr.append(arrA.pop())
    elif len(arrB) > 0:
        merged_arr.append(arrB.pop())
    
    print(merged_arr, "merged")


    return merged_arr

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
        merge(left, right)
        

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

