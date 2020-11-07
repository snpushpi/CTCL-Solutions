def main(M,N):
    #N+M C M
    num = N+M
    denom = 1 
    result = 1
    for i in range(N):
        result = (result*num)//denom
        print(result)
        num-=1
        denom+=1    
print(main(5,3))
