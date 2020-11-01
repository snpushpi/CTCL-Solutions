def edit_dist(s1,s2):
    m = len(s1)
    n = len(s2)
    L = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i and j:
                if s1[i-1]==s2[j-1]:
                    L[i][j]=L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i-1][j],L[i][j-1])
    print(L[m][n])
    return L[m][n]

def k_palindrome(s):
    if len(s)%2==0:
        s1 = s[:len(s)//2]
        s2 = s[len(s//2):][::-1]
        return len(s1)+len(s2)-2*edit_dist(s1,s2)
    else:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2+1:][::-1]
        print(s1,s2)
        return len(s1)+len(s2)-2*edit_dist(s1,s2)

print(k_palindrome("abcdeca"))