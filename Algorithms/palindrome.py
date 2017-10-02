import cProfile

def palindrome_chk(str1):

    for i in range(len(str1)):
        if str1[i]!=str[-i-1]:
            print "Not palindrome"
    else:
        print "Palindrome"



if __name__ == "__main__":

    palindrome_chk("madam")


