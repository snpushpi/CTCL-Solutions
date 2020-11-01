def possible_decodings(s):
    if len(s)==1:
        return 1
    if len(s)==2:
        if 10<=int(s)<=26:
            return 2
        else:
            return 1
    else:
        if 10<= int(s[-2]+s[-1])<=26:
            return possible_decodings(s[:-1])+possible_decodings(s[:-2])
        else:
            return possible_decodings(s[:-1])
print(possible_decodings('1234'))