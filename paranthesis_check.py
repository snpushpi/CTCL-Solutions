def main(string):
    stack = []
    for elt in string:
        if elt in {'{','[','('}:
            stack.append(elt)
        else:
            check_elt = stack.pop()
            if check_elt == '(' and elt==')':
                continue 
            elif check_elt == '{' and elt=='}':
                continue 
            elif check_elt == '[' and elt==']':
                continue 
            else:
                print('ji')
                return False 
    if len(stack)==0:
        return True 
    return False
print(main('{([])}'))