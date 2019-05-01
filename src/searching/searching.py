# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  
  while low <= high:
    middle = int((low+high)/2)
    if target < arr[middle]:
      high = middle-1
    elif target > arr[middle]:
      low = middle+1
    else:
      return middle
  
  return -1

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

  elif arr[middle] == target:
    return middle

  elif arr[middle] > target:
    return binary_search_recursive(arr, target, 0, middle)

  else:
    return binary_search_recursive(arr, target, middle, len(arr))  

arr1 = [3, 5, 6, 7, 9]
print(binary_search_recursive(arr1, 9, 0, len(arr1)-1))