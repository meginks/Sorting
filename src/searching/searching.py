# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code

   return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2
  if len(arr) == 0:
    return -1 # array empty
  elif len(arr) == 2: 
    if arr[0] == target: 
      return 0 
    else:
      return 1
  elif arr[middle] == target:
    return middle
  elif arr[middle] < target: 
    return binary_search_recursive(arr, target, middle, high)
  elif arr[middle] > target: 
    return binary_search_recursive(arr, target, low, middle)
  else:
    return 1
  # TO-DO: add missing if/else statements, recursive calls
