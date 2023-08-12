# Selection sort involves finding the minimum element in one pass through the array
# and then swapping it with the first postion of the unsorted part of the array
# Time complexity of selection sort is O(n^2) in all cases

def selection_sort(array):
    count = 0
    for i in range(len(array) - 1): #-1 because when only 1 element remians, it will be already
        print(array)
        minimum = array[i] # We set the minu=imum element to be the ith element
        minimum_index = i #  And the minimum index to be the ith index

        for j in range(i +1, len(array)): # Then we check the array from the i+1th element to the end
            count += 1
            if array[j] < minimum: # If a smaller element than the minimum element is found, we re-assign the minimu index
                minimum = array[j]
                minimum_index = j

        if minimum_index != i: # If minimum index has changed, i.e, a smaller element has been found, then we swap that element with the ith element
            array[minimum_index], array[i] = array[i], array[minimum_index]
    return (f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,19,45,2,0]

print(selection_sort(array))