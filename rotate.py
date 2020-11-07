def anti_clock(arr):
    return arr[-1]+arr[:-1]
def clock(arr):
    return arr[1:]+arr[0]
def main(string1,string2):
    if len(string1)!=len(string2):
        return False
    if string1 == string2:
        return True
    rstring = string1
    for i in range(1,len(string1)):
        rstring = anti_clock(rstring)
        if rstring==string2:
            return True
    rstring = string1
    for i in range(1,len(string1)):
        rstring = clock(rstring)
        if rstring==string2:
            return True
    return False
print(main('amazon','azonam'))
            

