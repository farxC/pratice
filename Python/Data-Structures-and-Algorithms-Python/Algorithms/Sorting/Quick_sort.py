# Quick Sort is another sorting algorithm which follows divide and conquer approach
# It requires to chose a pivot, then place all elements smaller than the pivot on the left of the pivot and all element larger on the right
# THen the array is partioned in the pivot postion and the left and right arrays follow the same procedure until the base case is reached.
# After each pass the pivot element occupies its correct position in the array.
# Time complexity in Best and Avarage cases is O(nlog N) whereareas in worst case it jumps up to O(n^2). Space complexity is O(log n)

# In this implementation, we will take the last element as pivot.
count= 0

def partition(array, left, right):
    smaller_index = left - 1
    pivot = array[right]
    for i in range(left, right):
        global count
        count += 1
        if array[i] < pivot:
            smaller_index += 1
            array[smaller_index], array[i] = array[i], array[smaller_index]
    array[smaller_index+1], array[right] = array[right], array[smaller_index +1]
    print(array)
    return (smaller_index + 1)

def quick_sort(array, left, right):
    if left < right:
        partitioning_index = partition(array, left, right)
        print(partitioning_index)
        quick_sort(array, left, partitioning_index - 1)
        quick_sort(array, partitioning_index + 1, right)


array = [5,9,3,10,45,2,0]
quick_sort(array, 0, (len(array)-1))

hello = 'Hello World'
print(hex(id(hello)))