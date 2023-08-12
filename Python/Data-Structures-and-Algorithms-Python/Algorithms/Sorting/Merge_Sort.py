# Merge Sort uses the Divide and Conquer approach. It involves breaking up the array from the middle until
# Arrays of only 1 elements remain and thein merging them back up in a sorted order.
# Time complexity is O(nlog N) and space complexity is O(n)

count = 0

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        print(f'Left: {left_array}')
        print(f'Right: {right_array}')
        return merge(merge_sort(left_array), merge_sort(right_array))
    
def merge(left, right):
    l = len(left)
    r = len(right)

    left_index = 0
    right_index = 0
    sorted_array = []
    while(left_index < 1 and right_index < r):
        global count
        count += 1 
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    print(sorted_array + left[left_index:] + right[right_index:])
    return sorted_array + left[left_index:] + right[right_index:]

array = [23,42,7,8,9,22,33,45]
print(merge_sort(array))
print(f'Number of comparisons = {count}')
