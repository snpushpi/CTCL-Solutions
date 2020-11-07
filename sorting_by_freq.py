def main(arr): #[4,4,4,3,3,3,2,2,2,2,1]
    count_dict = {}
    for elt in arr:
        if elt in count_dict:
            count_dict[elt]+=1 #count_dict = {2:4,4:3,1:1,3:3}
        else:
            count_dict[elt]=1
    value_set = {count_dict[elt] for elt in count_dict} #{3,4,1}
    #for each frequency, make a list of elements havig that frequency
    value_dict = {value:[] for value in value_set} # value_dict = {3:[],4:[],1:[]
    for elt in count_dict:
        value_dict[count_dict[elt]].append(elt) #value_dict = {3:[4,3],4:[2],1[1]}
    for elt in value_dict:
        value_dict[elt].sort() #value_dict = {3:[3,4],4:[2],1[1]}
    result_list = []
    for freq in value_dict: 3
        for elt in value_dict[freq]: [3,4]
            for i in range(freq): #3
                result_list.append(elt) #result_list.append(3,3,3,4,4,4)
    return result_list
