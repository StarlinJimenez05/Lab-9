def encode(password):
    _list = []
    for i in password:
        num = int(i)
        num = num + 3
        stringNum = str(num)
        _list.append(stringNum)
    s = ''
    result = s.join(_list)
    return result

print(encode("12345555"))


def decode(password):
    list = []
    for i in password:
        num = int(i)
        num = num - 3
        stringNum = str(num)
        list.append(stringNum)
    s = ''
    string = s.join(list)
    return string


print(decode('45678888'))