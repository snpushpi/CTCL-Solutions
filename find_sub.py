def find_sub_array(array,target):
    n = len(array)
    sum = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=array[j]
            if sum==target:
                return array[i:j+1]
print(find_sub_array([1, 4, 0, 0, 3, 10, 5],7))
            

        


