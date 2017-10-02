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



def ThreeHighestNumbers(arrayOfNumbers):
    PmaxNum1 = 0
    PmaxNum2 = 0
    PmaxNum3 = 0
    NMinNum1 = 0
    NMinNum2 = 0
    maxNumber = 0

    for num in arrayOfNumbers:
        if num < 0:
            if num < NMinNum1:
                NMinNum2 = NMinNum1
                NMinNum1 = num
            elif num < NMinNum2:
                NMinNum2 = num
        else:
            if num > PmaxNum1:
                PmaxNum3 = PmaxNum2
                PmaxNum2 = PmaxNum1
                PmaxNum1 = num

            elif num > PmaxNum2:
                PmaxNum3 = PmaxNum2
                PmaxNum2 = num

            elif num > PmaxNum3:
                PmaxNum3 = num

    maxNumber = PmaxNum1 * PmaxNum2 * PmaxNum3

    if maxNumber == 0:
        return []

    if maxNumber < PmaxNum1 * NMinNum1 * NMinNum2:
        return [PmaxNum1,NMinNum2,NMinNum1]
    else:
        return [PmaxNum1,PmaxNum2,PmaxNum3]




print ( ThreeHighestNumbers([100,-1,-3,-6,-9,0,4,3,21]))
print ThreeHighestNumbers([-9,1,6,-10,9])
print ThreeHighestNumbers([-10,-10,1,3,2])