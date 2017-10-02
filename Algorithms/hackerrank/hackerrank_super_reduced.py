def super_reduced_string(s):

    temp=[]
    temp.append(s[0])

    for i in range(1,len(s)):
        if not temp==[] and s[i]==temp[len(temp)-1] :
            temp.pop()
        else:
            temp.append(s[i])

    print temp

if __name__=="__main__":

    s='aaabccddd'

    super_reduced_string(s)