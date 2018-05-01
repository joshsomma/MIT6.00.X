s = 'aslasnalmgfamsanbjsbvsmsmdmsnqetrqwioanlsald'
result = []
temp_string = s[0]
for n in range(len(s)):
    if n == len(s) - 1:
        result.append(temp_string)
    else:
        if s[n] <= s[n+1]:
            temp_string +=  s[n+1]
        else:
            result.append(temp_string)
            temp_string = s[n+1]
print('Longest max substring in alphabetical order is: ',max(result,key=len))



    
    


