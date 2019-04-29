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
def bubble_sort( arr ):
    # loop through the array
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

list = [5, 3, 2, 1, 4]
print(bubble_sort(list))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr