def find Smallest(arr) # Find smallest
    smallest = arr[0] # Set value first element
    smallest_index = 0 # primary index
    for i in range(1, len(arr)):# List cycle
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return (smallest_index) # index smallest element
