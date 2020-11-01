def activity_selection_problem(start,finish):
    sorted_finish = sorted(finish)
    n = len(finish)
    f = finish.index(sorted_finish[0])
    result = [f]
    for i in range(1,n):
        print(start[finish.index(sorted_finish[i])],sorted_finish[i-1])
        if start[finish.index(sorted_finish[i])]>finish[result[-1]]:
            result.append(finish.index(sorted_finish[i]))
    return result
print(activity_selection_problem([1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9]))