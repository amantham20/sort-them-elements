
def bubbleSort(arr):
    """The functions sorts and return the array using bubble sorts

    Args:
        arr (List): input list of the files

    Returns:
        list: returns the sorted list of
    """
    n = len(arr)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubbleSort(arr)