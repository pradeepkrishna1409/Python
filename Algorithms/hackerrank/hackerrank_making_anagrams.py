def makingAnagrams(s1, s2):
    hm = [0] * 26

    for i in range(len(s1)):
        hm[ord(s1[i]) - ord('a')] += 1

    for i in range(len(s1)):
        hm[ord(s2[i]) - ord('a')] -= 1

    cnt=0
    for num in hm:
        cnt += abs(num)

    return cnt


s1 = raw_input().strip()
s2 = raw_input().strip()
result = makingAnagrams(s1, s2)
print(result)