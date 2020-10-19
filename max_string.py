def max_string(s):
    max_value = int(s[0])
    for i in range(q,len(s)):
        if int(s[i])>1:
            #max_value*=int(s[i])
            if i>=2:
                if s[i-2]=='0' and s[i-1]=='1':
                    max_value+=s[i]
                elif s[i-2]=='0' and s[i-1]=='0':
                    max_value+=s[i]
                elif s[i-2]=='1' and s[i-1]=='0':
                    max_value+=s[i]
                
            else:
                if 
        else:
            max_value+=int(s[i])