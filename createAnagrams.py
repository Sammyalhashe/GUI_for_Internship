def number_needed(a, b):
    num_need = 0
    a_dict = {}
    b_dict = {}
    res_dict = {}
    for chara in a:
        # could have just used defaultdict here
        if chara not in a_dict:
            a_dict[chara] = 1
        else:
            a_dict[chara] += 1
    for charb in b:
        if charb not in b_dict:
            b_dict[charb] = 1
        else:
            b_dict[charb] += 1
    for key, val in a_dict.items():
        if key in b_dict:
            res_dict[key] = abs(val - b_dict[key])
        elif key not in b_dict:
            num_need += val
            print("remove %d %s chars" % (val, key))
    for key, val in b_dict.items():
        if key not in a_dict:
            num_need += val
            print("remove %d %s chars" % (val, key))
    for key, val in res_dict.items():
        num_need += val
        print("remove %d %s chars" % (val, key))
    return num_need


a = 'Hello Darkness my old friend'
b = 'Ive come to talk to you again'

print(number_needed(a, b))
