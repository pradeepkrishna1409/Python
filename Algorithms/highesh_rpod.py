import sys
def highest_product(list_of_ints):
    size = len(list_of_ints)
    if size == 0:
        return 0
    first_max = -sys.maxsize-1
    second_max = -sys.maxsize-1
    third_max = -sys.maxsize-1
    first_min = sys.maxsize
    second_min = sys.maxsize

    for value in list_of_ints:
        if value>first_max:
            third_max = second_max
            second_max = first_max
            first_max = value
        elif value>second_max:
            third_max = second_max
            second_max = value
        elif value>third_max:
            third_max = value

        if value<first_min:
            second_min = first_min
            first_min = value
        elif value<second_min:
            second_min = value

    return max(first_max*second_max*third_max,first_max*first_min*second_min)

print ( highest_product([100,-1,-3,-6,-9,0,4,3,21]))
print ( highest_product([-9,1,6,-10,9]) )
print ( highest_product([-10,-10,1,3,2]) )