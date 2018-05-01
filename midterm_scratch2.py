def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    temp = L[:]
    for i in range(len(temp)):
        if not f(temp[i]):
            L.remove(temp[i])
    return len(L)


def f(s):
    return 'e' in s

# L = ['a', 'b', 'a']
# L = ['bat','bar','cat','scratch','bird','batch']
L = ['scare','bear','scar','bare','hare','car','care']
print(satisfiesF(L))
#run_satisfiesF(L, satisfiesF)