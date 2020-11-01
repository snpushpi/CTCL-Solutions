def longest_consecutive_character(s):
    n = len(s)
    l = [1 for i in range(n)]
    for i in range(1,n):
        if s[i]==s[i-1]:
            l[i]=l[i-1]+1
    m = 0
    for i in range(n):
        if l[i]>m:
            m=l[i]
    return m