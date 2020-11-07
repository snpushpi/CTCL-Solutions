def main(string):
    res = string[0]
    for i in range(1,len(string)):
        if string[i]!=res[-1]:
            res+=string[0]
    return res


