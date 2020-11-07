def main(string):
    window = {string[0]}
    window_length = 1
    maximum = 1
    for i in range(1,len(string)):
        print('ji')
        if string[i] not in window:
            window_length+=1
            window.add(string[i])
            
        else:
            window = {string[i]}
            window_length = 1
            for j in range(i-1,-1,-1):
                if string[j] not in window:
                    window_length+=1
                    window.add(string[j])
                else:
                    break
            
        maximum = max(maximum,window_length)
    return maximum
print(main('abababcdefababcdab'))





        