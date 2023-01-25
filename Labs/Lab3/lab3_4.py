def char_count(str):
    char_dict = {}
    char_collect = []
    for i in range(len(str)):
        char_dict[str[i]] = str.count(str[i])
    return char_dict
print(char_count('sadsad'))