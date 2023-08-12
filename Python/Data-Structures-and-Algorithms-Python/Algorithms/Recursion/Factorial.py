# Given a number, we have to return its factorial.
# For example, factorial(5) should return 5! = 5*4*3*2*1 = 120
# We can solve this recursively, or iteractively.
# First we are goint to solve it iteratively.

def iterative_factorial(number):
    f = 1
    for i in range(1, number + 1):
        f =1
        for i in range(1, number + 1):
            f = f * i
        return f
print(iterative_factorial(0))
print(iterative_factorial(5))

def recursive_factorial(number):
    if number <= 1:
        return 1
    else:
        return number * recursive_factorial(number - 1)
    
print(recursive_factorial(0))
print(recursive_factorial(5))
print(recursive_factorial(6))