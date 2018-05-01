animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['e'] = ['eagle', 'elephant', 'emu']
print(animals)

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    temp = {}
    for k in aDict:
        temp[k] = len(aDict[k])
    return max(temp)

print(biggest(animals))