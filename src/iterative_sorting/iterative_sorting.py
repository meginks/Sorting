# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # TO-DO: swap
    length = len(arr)-1
    for i in range(length):
        for j in range(0, length-i):
            cur_index = i
            min_index = cur_index
            min_value = min(arr) 
            min_index = arr.index(min_value) 
            arr[min_index], arr[i] = arr[i], arr[min_index] 
    return arr


# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):
    length = len(arr)-1
    for i in range(0, length):
        for j in range(0, length-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr