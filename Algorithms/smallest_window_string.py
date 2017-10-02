from collections import defaultdict
import sys

def minWindow(str, pattern):
    pattern_dict = defaultdict(int)
    print pattern_dict
    str_dict = defaultdict(int)
    print str_dict

    for ch in pattern:
        pattern_dict[ch] += 1

    print pattern_dict

    start = 0
    validCount = 0
    minSize = sys.maxint
    cur_chr=''

    for index in range(len(str)):

        cur_chr=str[index]

        if str[index] not in pattern_dict:
            continue

        if str_dict[str[index]] < pattern_dict[str[index]]:
            validCount += 1

        str_dict[str[index]] += 1

        print str_dict

        while validCount == len(pattern_dict):
            if str[start] not in pattern_dict:
                start += 1
            elif str_dict[str[start]] > pattern_dict[str[start]]:
                str_dict[str[start]] -= 1
                start += 1
            else:
                minSize = min(minSize, index-start+1)
                break

    return (minSize, start)

if __name__ == "__main__":
    print minWindow("awessomeabsm","sm")