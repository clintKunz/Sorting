# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
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

list = [3, 2, 4, 6, 3]
print(selection_sort(list))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr