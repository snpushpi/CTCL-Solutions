def main(arr):
    arr1 = [elt**2 for elt in arr]
    for i in range(len(arr1)):
        for j in range(i+1,len(arr)):
            if arr1[i]+arr1[j] in arr1:
                return True
    return False
        