'''
1) Start from the leftmost character and remove duplicates at left corner if there are any.
2) The first character must be different from its adjacent now. Recur for string of length n-1 (string without first character).
3) Let the string obtained after reducing right substring of length n-1 be rem_str. There are three possible cases
    a) If first character of rem_str matches with the first character of original string, remove the first character from rem_str.
    b) Else if the last removed character in recursive calls is same as the first character of the original string. Ignore the first character of original string and return rem_str.
    c) Else, append the first character of the original string at the beginning of rem_str.
4) Return rem_str
'''

# Recursively removes adjacent duplicates from str and returns
# new string. las_removed is a pointer to last_removed character
def removeUtil(string, last_removed):

    # If length of string is 1 or 0
    if len(string) == 0 or len(string) == 1:
        return string

    # Remove leftmost same characters and recur for remaining
    # string
    if string[0] == string[1]:
        last_removed = ord(string[0])
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]

        return removeUtil(string, last_removed)

    # At this point, the first character is definiotely different
    # from its adjacent. Ignore first character and recursively
    # remove characters from remaining string
    rem_str = removeUtil(string[1:], last_removed)
    print rem_str

    # Check if the first character of the rem_string matches
    # with the first character of the original string
    if len(rem_str) != 0 and rem_str[0] == string[0]:
        last_removed = ord(string[0])
        return (rem_str[1:])

    # If remaining string becomes empty and last removed character
    # is same as first character of original string. This is needed
    # for a string like "acbbcddc"
    if len(rem_str) == 0 and last_removed == ord(string[0]):
        return rem_str

    # If the two first characters of str and rem_str don't match,
    # append first character of str before the first character of
    # rem_str.
    return ([string[0]] + rem_str)

def remove(string):
    last_removed = 0
    return toString(removeUtil(toList(string), last_removed))

# Utility functions
def toList(string):
    x = []
    for i in string:
        x.append(i)
    return x

def toString(x):
    return ''.join(x)

# Driver program
string1 = "geeksforgeeg"
print remove(string1)