def caesar_cipher(str1):
    for i in range(len(str1)):

        if ord(str1[i]) >= 97 and ord(str1[i]) <= 122:
            n1 = ord(str1[i]) + 2

            if n1 > 122:
                n1 = 96 + n1 - 122

            str1[i] = chr(n1)
    print ''.join(str1)


caesar_cipher(list(('middle-outz')))