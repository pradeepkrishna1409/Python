def camel_case1(s):
    cnt = 1

    for ch in s:
        if ord(ch) >= 65 and ord(ch) <= 90:
            cnt += 1

    print cnt


def camel_case2(s):
    cnt = 1

    for ch in s:
        if ch.isupper():
            cnt += 1

    print cnt


print camel_case2('saveChangesInTheEditor')
