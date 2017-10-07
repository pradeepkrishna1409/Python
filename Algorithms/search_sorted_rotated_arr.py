def find_mininum_sorted_arr(a, low, high):
    if low == high:
        return a[low]

    if high < low:
        return -1

    mid = (low + high) / 2

    if high > mid and a[mid] > a[mid + 1]:
        #print 'pivot point is at ', mid
        return mid

    if low < mid and a[mid] < a[mid - 1]:
        #print 'pivot point is at ', mid-1
        return mid - 1

    if a[mid] <= a[low]:
        return find_mininum_sorted_arr(a, low,mid-1)

    return find_mininum_sorted_arr(a,  mid + 1,high)


def search_sorted_rotated_arr(a, k, n):
    pivot = find_mininum_sorted_arr(a, 0, n)

    if a[pivot] == k:
        return pivot

    if a[0] <= k:
        return binary_search(a, 0, pivot - 1, k)

    return binary_search(a, pivot + 1, len(a) - 1, k)


def binary_search(a, low, high, k):
    if low > high:
        return -1

    mid = (low + high) / 2

    if a[mid] == k:
        return mid
    elif a[mid] > k:
        return binary_search(a, low, mid - 1, k)
    else:
        return binary_search(a, mid + 1, high, k)


if __name__ == "__main__":
    k = 3
    a = [5, 6, 7, 8, 9, 10, 1, 2, 3]

    print "Element ", k, ' is found at index ', search_sorted_rotated_arr(a, k, len(a) - 1)
