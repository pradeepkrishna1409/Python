
def bubble_sort(lst):
    print lst
    pass_num = len(lst)-1
    exchange=True

    while pass_num>0 and exchange:
        for i in range(pass_num):
            if lst[i] > lst [i+1]:
                lst[i],lst [i+1]=lst [i+1],lst[i]
    pass_num = pass_num-1

    print lst


def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

if __name__ == "__main__":

    lst = [23,99,5,67,22]
    bubble_sort(lst)
