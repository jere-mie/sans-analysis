# Functions related to curve fitting

# modified binary search where we only care about matching the element most close to 'x' within a threshhold (0.05 here)
def f_bs(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0 
    while low <= high: 
        mid = (high + low) // 2
        if abs(arr[mid]-x) < 0.05:
            return mid
        elif arr[mid] < x:
            low = mid + 1 
        else:
            high = mid - 1
    return -1

# uses f_bs to transform a larger array into a wanted x range
def change_x(x_old, y_old, x_wanted):
    return [y_old[f_bs(x_old, i)] for i in x_wanted]


# gets the scaling factor of vbad to vgood in an inefficient way...
# to make it more efficient, change the for loop to go in range(0, len(vbad), n)
# where n is some arbitrary integer, and then change the return statement to
# return sumDiff/(len(vbad)/n) for that same n
def dynamicScale(vbad, vgood):
    sumDiff = 0
    for i in range(len(vbad)):
        sumDiff+= vgood[i]/vbad[i]
    return sumDiff/len(vbad)
