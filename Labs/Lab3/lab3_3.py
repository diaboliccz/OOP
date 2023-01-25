def is_plusone_dictionary(d):
    count = 0
    keys_list = []
    values_list = []
    for key, value in d.items():
        keys_list.append(key)
        values_list.append(value)
    for i in range(len(keys_list)-1):
        if values_list[i] - keys_list[i] == 1:
            if keys_list[i+1] - keys_list[i] == values_list[i+1] - values_list[i]:
                count+=1
    if count+1 == len(d):
        return True
    return False

print(is_plusone_dictionary({1:2, 3:4, 5:6}))