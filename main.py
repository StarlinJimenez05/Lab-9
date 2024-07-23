def encode(password):
    _list = []
    for i in password:
        i = int(i)
        i = i +3
        _list.append(i)
    s = ' '
    result= s.join(_list)
    return result

print(encode("12345555"))


