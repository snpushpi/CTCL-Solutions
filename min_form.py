def main(string):
    dp = [[0 for i in range(len(string))] for j in range(len(string))]
    for i in range(len(string)):
        dp[i][i]=0 #'abcda'
    n = len(string)
    for L in range(2,n+1):
        for i in range(n-L+1):
            j = i+L-1
            print((i,j))
            if string[i]==string[j]:
                if L==2:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i+1][j-1]
                    if i==0 and j==4:
                        print(dp[i][j])
            else:
                dp[i][j]= 1+min(dp[i+1][j],dp[i][j-1])
            if i==0 and j==4:
                print(dp[i][j])
    return dp
print(main('abcda'))
