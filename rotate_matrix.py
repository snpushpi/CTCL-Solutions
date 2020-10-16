def rotate_matrix(m):
    n = len(m)
    if n%2==0:
        for i in range(n//2):
            for j in range(n//2):
                a = m[i][j]
                b = m[j][n-i-1]
                c = m[n-i-1][n-j-1]
                d = m[n-j-1][i]
                m[i][j] = d
                m[j][n-i-1] = a
                m[n-i-1][n-j-1] = b
                m[n-j-1][i] = c
    else:
        for i in range(n//2+1):
            for j in range(n//2):
                a = m[i][j]
                b = m[j][n-i-1]
                c = m[n-i-1][n-j-1]
                d = m[n-j-1][i]
                m[i][j] = d
                m[j][n-i-1] = a
                m[n-i-1][n-j-1] = b
                m[n-j-1][i] = c
        
    return m
print(rotate_matrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))
    
