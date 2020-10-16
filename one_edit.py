def insert(s,t):
    for i in range(len(s)):
        if t[:i]+t[i+1:]==s:
            return True
    return False

def remove(s,t):
    for i in range(len(s)):
        if s[:i]+s[i+1:]==t:
            return True
    return False
def replace(s,t):
    for i in range(len(s)):
        if s[:i]+s[i+1:]==t[:i]+t[i+1:]:
            return True
    return False
def main(s,t):
    if len(s)-len(t)==1:
        return remove(s,t)
    elif len(s)==len(t)-1:
        return insert(s,t)
    elif len(s)==len(t):
        return s==t or replace(s,t)
    else:
        return False
    
print(main('asfer','asert'))