def main(arr):
    n = len(arr)
    C = [[0 for i in range(n)] for j in range(n)]
    P = [[False for i in range(n)] for j in range(n)]
    for i in range(n):
        C[i][i]=0
        P[i][i]=True
    
    for L in range(2,n+1):
        for i in range(n-L+1):
            j = i-L+1
            if L==2:
                P[i][j] = (arr[i]==arr[j])
            else:
                P[i][j]= ((arr[i]==arr[j]) and (P[i+1][j-1]))
            if P[i][j]:
                C[i][j]=0
            else:
                C[i][j] = float('inf')
                for k in range(i,j):
                    print('hi')
                    C[i][j] = min(C[i][j],1+C[i][k]+C[k+1][j])
                    
    print(C)
    return C[0][n-1]
print(main('google'))        