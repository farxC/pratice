# Given a String, we need to reverse it using recursion (and iteration)
# For example, input = "Rafael Fodinha fodão cala a boca de geralzao", output = "Inverso kkkk"


# For the first example we will implement the iterative solution
def iterative_reverse(string): # Here we use a second string to store the reversed version
    reversed_string = ''
    for i in range(len(string)):
        reversed_string = reversed_string + string[len(string)-i-1]
    return reversed_string

print(iterative_reverse("Rafael Fodinha fodao cala a boca de geralzao"))

# Here we append the string backwards into the original string itself and then slice it
# Time Complexity = O(n). Space Complexity = 0(n)

def second_iterative_reverse(string):
    original_length = len(string)
    for i in range(original_length):
        string = string + string[original_length - i - 1]
    string = string[original_length:]
    return string

print (second_iterative_reverse("rafinha mito kkkkkk"))

def recursive_reverse(string):
    print(string)
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]
    
print(recursive_reverse("Rafael foda demais kk"))

a = 'Rafael foda'
print(a[0:2])