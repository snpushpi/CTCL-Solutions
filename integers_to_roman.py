def integer_to_roman(number):
    num = [1,4,5,9,10,40,50,100,400,500,900,1000]
    num.reverse()
    sym = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    sym.reverse()
    i = 0
    res_str = ''
    while number:
        if number >=num[i]:
            d = number//num[i]
            r = number%num[i]
            for j in range(d):
                res_str+=sym[i]
            number = r 
            i+=1
    return res_str


