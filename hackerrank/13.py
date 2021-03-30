def swap_case(s):
    res = ''
    res = ''.join([i.lower() if i.isupper() else i.upper() for i in s])
    return res

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result