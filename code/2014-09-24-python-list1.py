# coding=utf-8


list1 = [1, 2, 3, 1]
s = set(list1)
print s


def _remove_duplicate(dict_list, keys):
    seen = set()
    new_dict_list = []
    for dic in dict_list:
        t_dict = {k: dic[k] for k in keys}
        t_tup = tuple(t_dict.items())
        if t_tup not in seen:
            seen.add(t_tup)
            new_dict_list.append(dict)

    return new_dict_list


dict_list = [{'new': 1, 'old': 'hello'}, {'new': 2, 'old': 'world'}, {'new': 2, 'old': 'zzn'}]
keys = ['new']
print _remove_duplicate(dict_list, keys)

