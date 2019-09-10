# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # ^^^ that confused me again. . . . . 
    i = 0
    j = 0 
    merged_arr = [] 
    while i < len(arrA) and j < len(arrB): 
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1 
        else: 
            merged_arr.append(arrB[j])
            j += 1
    merged_arr.extend(arrA[i:])
    merged_arr.extend(arrB[j:])
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) < 2: 
        new_array = arr[:len(arr)]
        return new_array
    midpoint = len(arr) // 2
    left_array = arr[0:midpoint]
    right_array = arr[midpoint:len(arr)]
    new_left_array = merge_sort(left_array)
    new_right_array = merge_sort(right_array)
    new_array = merge(new_left_array, new_right_array)
    return new_array
        
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    start2 = mid + 1
    if arr[mid] <= arr[start2]: 
        return arr 
    while start <= mid and start2 <= end:
        if arr[start] <= arr[mid]:
            start += 1 
        else:
            value = arr[start2] 
            index = mid+1 
            while index != start:
                arr[index] = arr[index-1]
                index -= 1
            arr[start] = value 
            start += 1 
            mid += 1 
            start2 += 1
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if l <= r and l > 0:
        middle = l + (r - l) // 2 
        merge_sort_in_place(arr, l, r)
        merge_sort_in_place(arr, middle+l, r)
        merge_in_place(arr, l, middle, r)
    else: 
        return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
