def ignore_string(string):
    count_dic = {}
    result_string = ''
    for char in string:
        if char in count_dic:
            count_dic[char]+=1
        else:
            count_dic[char]=1
        if count_dic[char]%2==1:
            result_string+=char
    return result_string
print(ignore_string("It is a long day dear"))