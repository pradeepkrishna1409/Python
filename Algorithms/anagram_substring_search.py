
# def compare_texts(lst_pat,lst_text):
#
#     for i in range(257):
#         if lst_pat[i] != lst_text[]


def anagram_search(pattern,text):

    lst_pat = [0] * 256
    lst_text = [0] * 256

    len_pat = len(pattern)
    len_text = len(text)


    for i in range(len(pattern)):
        lst_pat[ord(pattern[i])] += 1
        lst_text[ord(text[i])] += 1

    if lst_pat == lst_text:
        print "Anagram at index "
    else:
        print "Not a anagram"

    for i in range(len(pattern),len(text)):

        lst_text[ord(text[i])] += 1
        lst_text[ord(text[i-len_pat])] -= 1

        print text[i]
        print text[i-len_pat]

        if lst_pat == lst_text:
            print "Anagram at index " + str(i-len_pat)
        else:
            print "Not a anagram"


if __name__ =="__main__":

    pattern="ABCD"
    text='EACDGABCDA'

    anagram_search(pattern,text)




