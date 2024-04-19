import random


def simple_list():
    list_dict = []
    for i in range(10):
        dict = {
            'id': i,
            'age': random.randint(1, 100)
        }
        list_dict.append(dict)
    return list_dict


def sort_list(dicts):
    return sorted(dicts, lambda x: x.get('age'))
