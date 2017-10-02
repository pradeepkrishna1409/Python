import random



def shuffle_in_place(array):
    for index in range(len(array)):
        swap = random.randint(0,len(array)-1)
        new_list[swap] = array[index]
    print new_list


alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list=alist

print shuffle_in_place(alist)


