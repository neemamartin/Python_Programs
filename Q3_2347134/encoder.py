

def generate_padding(index):
    return '0' * index + '1' + '0' * (7 - index)

def EncodeQR(name):
    if 0 < len(name) <= 5:
        return ''.join(generate_padding(i) + format(ord(char), '08b') for i, char in enumerate(name))
    else:
        return "Use at least 1 character and\nDo not enter word having more than 5"

