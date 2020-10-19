def largest_subset_fib(l):
    m = max(l)
    fib_set= [0,1]
    last_elt = 1
    while last_elt<=m:
        new_elt = fib_set[-1]+fib_set[-2]
        fib_set.append(new_elt)
        last_elt = new_elt
    print(fib_set)
    return set(fib_set) & set(l)
print(largest_subset_fib([0, 2, 8, 5, 2, 1, 4, 
                  13, 23]))
