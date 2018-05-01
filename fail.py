my_list = [[[3],'cat',42], [['b',[3],'goat'], 4, 5], 6]

def flatten(aList):
    new_list = []
    for i in aList:
        if type(i) != type([]):
            new_list.append(i)
        else:
            new_list.extend(flatten(i))
    return new_list

print(flatten(my_list))