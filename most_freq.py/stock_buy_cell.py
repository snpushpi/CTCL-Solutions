def main(arr,k):
    dp = [[0]*(len(arr)+1)]*(k+1)
    for i in range(1,k+1):
        prev_diff = -float('inf')
        for j in range(1,len(arr)+1):
            prev_diff = max(prev_diff,dp[i-1][j-1]-arr[j-1])
            dp[i][j] = max(dp[i][j-1],prev_diff+arr[j])
    return dp[k][n-1]
print(main())

