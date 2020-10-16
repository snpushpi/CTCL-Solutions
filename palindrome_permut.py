def counter(s):
    result = {}
    for c in s:
        if c in result:
            result[c]+=1
        else:
            result[c]=1
    return result

def palindrome(s):
    count = 0
    result_dict = counter(s)
    for value in result_dict:
        if result_dict[value]%2==1:
            count+=1
    return count<=1
         
print(palindrome('accnna'))