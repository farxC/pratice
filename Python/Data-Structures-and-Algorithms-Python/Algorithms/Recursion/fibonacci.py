# Given a number, we have to return the number that index of the fibonacci sequence.
# For example, fibonacci(5) should return 5 as the 5th index (starting from 0) of the fibonacci sequence is the number 5
# Again, we will do both the iterative and recursive solutions


def iterative_fibonacci(index):
    first_number = 0
    second_number = 1

    if index == 0:
        return first_number
    if index == 1:
        return second_number
    for i in range(2, index + 1):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
    return third_number

print(iterative_fibonacci(0))
print(iterative_fibonacci(5))



def recursive_fibonacci(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return recursive_fibonacci(index - 1) + recursive_fibonacci(index - 2)

print(recursive_fibonacci(0))
print(recursive_fibonacci(7))