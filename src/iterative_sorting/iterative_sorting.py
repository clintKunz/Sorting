import random
# TO-DO: Complete the selection_sort() function below 
def insertion_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        temp = arr[i]
        j = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        # TO-DO: swap
        arr[j] = temp

    return arr

def selection_sort( arr ):
    for i in range(0, len(arr - 1)):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps_occurred = True

    while swaps_occurred:
        swaps_occurred = False

        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swaps_occurred = True

    return arr    

def selection_sort2( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort2( arr ):
    # loop through the array
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# quick sort
def quick_sort(arr, low, high):
    if low >= high:
        return arr
    
    else:
        pivot_index = low

        for i in range(low, high):

            if arr[i] < arr[pivot_index]:
                temp = arr[pivot_index+1]
                arr[pivot_index+1] = arr[i]
                arr[i] = temp

                temp = arr[pivot_index]
                arr[pivot_index] = arr[pivot_index+1]
                arr[pivot_index+1] = temp
                pivot_index += 1

    arr = quick_sort(arr, low, pivot_index)

    arr = quick_sort(arr, pivot_index+1, high)
    
    return arr

l = [random.randint(0,1000) for i in range(0,100)]
quick_sort(l, 0, len(l))
print(l)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr