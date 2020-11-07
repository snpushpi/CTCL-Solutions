def main(string, last_removed):
    if len(string)==0 or len(string)==1:
        return string
    if string[0]==string[1]:
        last_removed = string[0]
        while string[0]==string[1] and len(string)>1:
            string = string[1:]
        string = string[1:]
        return main(string,last_removed)
    rem_string = main(string[1:],last_removed)
    if len(rem_string)==0:
        return rem_string
    elif rem_string[0]==string[0]:
        return rem_string[1:]
    else:
        string[0]+rem_string
print(main('aaxxxay',''))

    