
def Binary_search(a,item):
    found=False

    low=0
    high=len(a)


    while not found and low<=high:
        mid=low + (high-low)/2

        if a[mid]==item:
            found=True
            print "Found item at position ", mid+1
        elif a[mid]>item:
            high=mid-1
        elif a[mid]<item:
            low=mid+1


a = [10,19,23,44,67,89,123,5646]

Binary_search(a,89)