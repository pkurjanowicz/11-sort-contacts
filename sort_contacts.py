def sort_contacts(dictionary):
    new_list = []
    for key in dictionary:
        sub_list_tuple = ()
        sub_list_list = list(sub_list_tuple)
        var1, var2 = dictionary[key]
        sub_list_list.append(key)
        sub_list_list.append(var1)
        sub_list_list.append(var2)
        sub_list_tuple = tuple(sub_list_list)
        new_list.append(sub_list_tuple)
    new_list.sort()
    return new_list
