


def find_mininum_sorted_arr(a,low,high):

    if low == high:
        return a[low]

    mid = (low+high)/2

    if high > mid and a[mid]> a[mid+1]:
        return a[mid+1]

    if low < mid and a[mid]< a[mid-1]:
        return a[mid]

    if a[mid]> a[low]:
        return find_mininum_sorted_arr(a,mid-1,high)

    return find_mininum_sorted_arr(a,low,mid+1)


if __name__=="__main__":

    a = [5, 6, 7, 8, 9, 10, 1, 2, 3]
   print find_mininum_sorted_arr(a,0,len(a)-1)