### Find number of consecutive characters

def alternatingCharacters(s):
    i = 0
    cnt = 0

    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            cnt += 1

        i += 1

    print cnt


if __name__ == "__main__":
    result = alternatingCharacters('AAABBB')
    print(result)