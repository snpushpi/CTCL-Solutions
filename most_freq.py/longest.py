def main(arr):
    dp = [[True]*len(arr)]*len(arr)
    n = len(arr)
    maximum = ''
    #i is difference between start vertex and end vertex, length is i+1
    for i in range(1,len(arr)):
        for j in range(n-i):
            if arr[j]!=arr[j+i]:
                dp[j][j+i] = False
            else:
                if i==1:
                    dp[j][j+i]=True
                    if i+1>len(maximum):
                        maximum = arr[j:j+i+1]
                        print(maximum)
                else:
                    print('ji',j,j+i)
                    dp[j][j+i] = dp[j+1][j+i-1]
                    if dp[j][j+i] and i+1>len(maximum):
                        maximum = arr[j:j+i+1]
                        print(maximum)
    print(dp)
    return maximum
print(main("forgeeksskeegfor"))
